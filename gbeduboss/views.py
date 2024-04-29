from datetime import datetime, date
from http.client import HTTPResponse
import uuid
import requests
import json
import os



from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import update_session_auth_hash
from django.core.paginator import Paginator
from django.contrib.auth.models import AnonymousUser
from django.core.mail import EmailMessage
from django.conf import settings
from django.http import Http404
from django.db.models import F


from guest_user.decorators import allow_guest_user
from taggit.models import Tag
from paypal.standard.forms import PayPalPaymentsForm
import yagmail
from dotenv import load_dotenv
_ = load_dotenv()



from beatcart.models import *


from .forms import *
from .models import *
from beats.models import *



email_address = os.environ.get("EMAIL_ADDRESS")
email_password = os.environ.get("EMAIL_PASSWORD")
receiver = os.environ.get("TO")

yag = yagmail.SMTP(f'{email_address}', f'{email_password}')
# Create your views here.




def index(request):
    beatcart= Beatscart.objects.filter(user__username = request.user.username, item_paid=False)
    albumcart= Albumcart.objects.filter(user__username = request.user.username, item_paid=False)
    banner = Banner.objects.get()
    service = Services.objects.get()
    advert = Advert.objects.get()
    one = Subdescription.objects.filter(one=True)
    two = Subdescription.objects.filter(two=True)
    three = Subdescription.objects.filter(three=True)
    four = Subdescription.objects.filter(four=True)
    five = Subdescription.objects.filter(five=True)
    six = Subdescription.objects.filter(six=True)
    beat = Beats.objects.all()
    album = Album.objects.all()

    if request.method == 'POST':
        news = request.POST =['newsletter']
        if news:

            news = Newsletter.objects.create(email= news)
            news.save()

        # newsletter_dict =[]
        # for newslet in news:
        #     newsletter_dict.append(newslet)

        # # to notify the owner about the filed form
        # to_1 = f'{news}'
        # # to_2 = 'mdpeter28@gmail.com'
        # subject = 'Newsletter Letters Subscribers'
        # body_1 = f'You Subscribed to our newsletter',
        # # body_2 = f'You have new subscriber(s) f"{newsletter_dict}"',
        

        # yag.send(to = to_1, subject = subject, contents = body_1)
        # yag.send(to = to_2, subject = subject, contents = body_2)
            

    context={
        'banner': banner,
        'service': service,
        'one': one,
        'two': two,
        'three': three,
        'four': four,
        'five': five,
        'six': six,
        'advert': advert,
        'beat': beat,
        'album': album,
        'beatcart':beatcart,
        'albumcart':albumcart,
        # 'news':news,
    }

    return render (request, 'index.html', context)


def musiclist(request,tag_slug=None,category_slug=None, genre_slug=None):
    beatcart= Beatscart.objects.filter(user__username = request.user.username, item_paid=False)
    albumcart= Albumcart.objects.filter(user__username = request.user.username, item_paid=False)
    cats = Categories.objects.all()
    # artist = All_artist.objects.all()
    genrs = Genre.objects.all()
    buy = Beats.objects.filter(buy=True, display= True)
    freedownload = Beats.objects.filter(freedownload=True,display= True)

    pag = Paginator(Beats.objects.all(),2)
    page_number = request.GET.get('page',all)
    beatlist= pag.get_page(page_number)

    pag = Paginator(Album.objects.all(),1)
    page_number = request.GET.get('page',all)
    albumlist= pag.get_page(page_number)

    tag= None
    taged = None
    category= None
    genre = None
    # if(Categories.objects.filter(slug=category_slug)):
    #     cats=Beats.objects.filter(category__slug= category_slug)

    if category_slug:
        category = get_object_or_404(Categories,slug=category_slug)
        beatlist= Beats.objects.filter(category=category)


    if genre_slug:
        genre = get_object_or_404(Genre,slug=genre_slug)
        beatlist= Beats.objects.filter(genre=genre)


    if tag_slug:
        tag = get_object_or_404(Tag,slug=tag_slug)
        beatlist=Beats.objects.filter(tags__in=[tag])
    
    if tag_slug:
        taged = get_object_or_404(Tag,slug=tag_slug)
        albumlist= Album.objects.filter(tags__in=[taged])

    return render(request, 'music/musiclist.html',
    {'beatlist':beatlist, 'albumlist':albumlist,
    'cats':cats,'buy':buy,'freedownload':freedownload,'beatcart':beatcart,'albumcart':albumcart,'genrs': genrs,})


def download(request, id):
    song = get_object_or_404(Beats, beats_id =id)
    file_path = song.beats.path

    if file_path.exist():
        with open(file_path,'rb') as file:
            response=HTTPResponse(file.read(), content_type="audio/mpeg")
            response['Content-Disposition']= 'attachment; filename="{}"'.format(song.beats.name)
            return response
    raise Http404


def playsong(request, id,slug):
    url = request.META.get('HTTP_REFERER')
    # number_of_comment = Comment.objects.filter(playsong_com__gt=F('playsong_com_id'))
    beatcart= Beatscart.objects.filter(user__username = request.user.username, item_paid=False)
    albumcart= Albumcart.objects.filter(user__username = request.user.username, item_paid=False)
    beat= Beats.objects.get(beats_id=id)
    beatcom = Comment.objects.filter(playsong_com=id)
    beats = CommentForm(instance=beat)
    if request.method == 'POST':
        beats = CommentForm(request.POST, instance=beat or None)
        if beats.is_valid():
            comment = beats.cleaned_data['comment']
            d= beats.save(commit=False)
            d.user= request.user
            c = Comment(playsong_com=beat, user= d.user, comment= comment, date=datetime.now())
            c.save()
            return redirect('albumsong', beat.pk, beat.slug )
    else:
        beats = CommentForm()

    nextbeat = Number_beat.objects.filter(pk__gt = beat.pk).order_by('id').first()
    lastbeat = Number_beat.objects.filter(pk__lt= beat.pk).order_by('id').last()
    #https://www.djangotemplatetagsandfilters.com/filters/urlencode/
  

    context={
        'beat':beat,
        'beatcom':beatcom,
        'beats':beats,
        'nextbeat':nextbeat,
        'lastbeat':lastbeat,
        'beatcart':beatcart,
        'albumcart':albumcart,
        # 'number_of_comment':number_of_comment,
    }

    return render(request, 'music/playsong.html', context)

def remove_beat_comment(request, id,slug):
    beat= Beats.objects.get(pk=id)
    deletecomment = request.POST['deletebeat']
    Comment.objects.filter(pk=deletecomment).delete()
    return redirect('playsong', beat.pk, beat.slug)


def albumsong(request, id,slug):
    beatcart= Beatscart.objects.filter(user__username = request.user.username, item_paid=False)
    albumcart= Albumcart.objects.filter(user__username = request.user.username, item_paid=False)
    album = Album.objects.get(pk= id)
    albu = Beats.objects.filter(album_name= id)
    albcom = Comment.objects.filter(comment_beat=id)
    albums = CommentForm(instance=album)
    if request.method == 'POST':
        albums = CommentForm(request.POST, instance=album)
        if albums.is_valid():
            # pics = request.POST['picture']
            comment = albums.cleaned_data['comment']
            d= albums.save(commit=False)
            d.user= request.user
            c = Comment(comment_beat=album, user= d.user, comment= comment, date=datetime.now())
            c.save()
            return redirect('albumsong', album.pk, album.slug )
    else:
        albums = CommentForm()
    
    nextbeat = Number_album.objects.filter(pk__gt = album.pk).order_by('id').first()
    lastbeat = Number_album.objects.filter(pk__lt= album.pk).order_by('id').last()


    context={
        'album':album,
        'albu':albu,
        'albums':albums,
        'albcom':albcom,
        'nextbeat':nextbeat,
        'lastbeat':lastbeat,
        'beatcart':beatcart,
        'albumcart':albumcart,
    }

    return render(request, 'music/albumsong.html', context)

def remove_album_comment(request, id, slug):
    album= Album.objects.get(pk=id)
    deletecomment = request.POST['deletealbum']
    Comment.objects.filter(pk=deletecomment).delete()
    return redirect('albumsong', album.pk, album.slug)


def booking(request):
    beatcart= Beatscart.objects.filter(user__username = request.user.username, item_paid=False)
    albumcart= Albumcart.objects.filter(user__username = request.user.username, item_paid=False)
    if request.method == 'POST':
        if request.POST.get('submit')== "submit1":
           form = StudioForm()
           if request.method == 'POST':
                form = StudioForm(request.POST, request.FILES)
                if form.is_valid():
                    d= form.cleaned_data['name']
                    c= form.cleaned_data['phone']
                    b= form.cleaned_data['email']
                    a= form.cleaned_data['file']
                    m= form.cleaned_data['message']
                    form.save()
                    messages.success(request, 'Boking was successfull, an email will be sent as soon as possible')

                    # to notify the owner about the filed form
                    to = f'{receiver}'
                    subject = 'Studio Booking'
                    body = f'A client {d}, with the phone number {c} and email {b} sent this file {a}. \n Message;  \n{m}.',
                    
                    yag.send(to = to, subject = subject, contents = body)

                    return redirect('booking')
                    # email =EmailMessage(
                    #     'Studio Booking alert !', #subject
                    #     f'A client {d}, with the phone number {c} and email {b} sent this file {a}. \n Message; \n{m}.', #message
                    #     settings.EMAIL_HOST_USER, #HOST EMAIL
                    #     ['mdpeter28@gmail.com'], #receiver
                    # )
                    # email.fail_silently=False
                    # email.send()
                    # return redirect('booking')

                    
                else:
                    messages.error(request, form.errors)
                    return redirect('booking')



        elif request.POST.get('submit')== "submit2":
           cform = SongForm()
           if request.method == 'POST':
                cform = SongForm(request.POST, request.FILES)
                if cform.is_valid():
                    d= cform.cleaned_data['name']
                    c= cform.cleaned_data['phone']
                    b= cform.cleaned_data['email']
                    a= cform.cleaned_data['file']
                    m= cform.cleaned_data['message']
                    cform.save()
                    messages.success(request, 'Song sent successfull, an email will be sent as soon as possible')

                    # to notify the owner about the filed form
                    to = f'{receiver}'
                    subject = 'Song Repairing'
                    body = f'A client {d}, with the phone number {c} and email {b} sent this file {a}. \n Message;  \n{m}.',
                    
                    yag.send(to = to, subject = subject, contents = body)
                    return redirect('booking')
                else:
                    messages.error(request, cform.errors)
                    return redirect('booking')

    form = StudioForm()
    cform = SongForm()

    return render (request, 'booking/booking.html',{'cform':form, 'form':form,'beatcart':beatcart,'albumcart':albumcart})



# ############ Authentication ############### #
def register(request):
    form = SignupForm() #instantiate the signupform for get request
    if request.method == 'POST':
        image = request.POST['image']
        form = SignupForm(request.POST)
        if form.is_valid():
            form = form.save()
            newsave = Comment(user= form)
            newsave.name = form.username
            newsave.pics= image
            newsave.save()
            login(request, form)
            messages.success(request, 'You can now book your appointment with the doctor')
            return redirect('index')
        else:
            messages.error(request, form.errors)
            return redirect('signup')
    
    context={
        'form': form,
    }


    return render (request, 'auth/register.html', context)


def signin(request):
    url = request.META.get('HTTP_REFERER')
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username= username, password= password)
        if user is not None:
            login(request, user)
            messages.success(request, f'Welcome back {user.first_name.title()}')
            return redirect('index')
        else:
            messages.info(request, 'Make sure both the username and password is correct')
            return redirect(url)

    return render(request, 'auth/signin.html')


def loggout(request):
    logout(request)
    return redirect('signin')

# ############ Authentication End ############### #


# ################# CARTS ##################### #
@allow_guest_user
def addtocart(request):
    beatcart = uuid.uuid4()
    beat_code = beatcart
    if request.method == 'POST':

        # quantity is displayed globally in the function
        addquantity = int(request.POST['quantity'])      
        try:
            addidd = request.POST['albumid']
            albumid= Album.objects.get(pk=addidd)

            # instantiate the cart for prospertive users
            # this works for both guest users and signed-in users
            albums = Albumcart.objects.filter(user__username=request.user.username,item_paid=False)
            if albums:
                proalbums =Albumcart.objects.filter(album_id =albumid.pk, quantity= addquantity,user__username=request.user.username).first()
                if proalbums:
                    proalbums.quantity = addquantity
                    proalbums.save()
                    messages.success(request, 'Item has been added to your cart')
                    return redirect('musiclist')

                else:
                    newcart = Albumcart()
                    newcart.user=request.user
                    newcart.album = albumid
                    newcart.quantity = addquantity
                    newcart.order_no= albums[0].order_no
                    newcart.item_paid =False
                    newcart.save()
                    messages.success(request, 'Item has been added to your cart')
                    return redirect('musiclist')
            else:
                newcart = Albumcart()
                newcart.user=request.user
                newcart.album = albumid
                newcart.quantity = addquantity
                newcart.order_no=beat_code
                newcart.item_paid=False
                newcart.save()
                messages.success(request, 'Item has been added to your cart')
                return redirect('musiclist')

        except:
            addid = request.POST['beatid']
            beatid = Beats.objects.get(pk=addid)

            # instantiate the cart for prospertive users
            # this works for both guest users and signed-in users
            beats = Beatscart.objects.filter(user__username=request.user.username,item_paid=False)

            if beats:
                probeats =Beatscart.objects.filter(beat_id =beatid.pk, quantity= addquantity,user__username=request.user.username).first()
                if probeats:
                    probeats.quantity = addquantity
                    probeats.save()
                    messages.success(request, 'Item has been added to your cart')
                    return redirect('musiclist')

                else:
                    newcart = Beatscart()
                    newcart.user=request.user
                    newcart.beat = beatid
                    newcart.quantity = addquantity
                    newcart.order_no= beats[0].order_no
                    newcart.item_paid =False
                    newcart.save()
                    messages.success(request, 'Item has been added to your cart')
                    return redirect('musiclist')
            else:
                newcart = Beatscart()
                newcart.user=request.user
                newcart.beat = beatid
                newcart.quantity = addquantity
                newcart.order_no=beat_code
                newcart.item_paid=False
                newcart.save()
                messages.success(request, 'Item has been added to your cart')
                return redirect('musiclist')


@allow_guest_user
def cart(request):
    beatcart= Beatscart.objects.filter(user__username = request.user.username, item_paid=False)
    albumcart= Albumcart.objects.filter(user__username = request.user.username, item_paid=False)

    total= 0
    tota= 0
    apple_url =os.environ.get("APPLE_URL")
    for item in beatcart:
        if item.beat:
            total += item.beat.price + item.quantity
        else:
            total == 0
    
    for item in albumcart:
        if item.album:
            tota += item.album.price + item.quantity
        else:
            tota == 0

    if total and tota != 0:
        fulltotal = (total - 1) + (tota - 1)
    elif total ==0 and tota != 0:
        fulltotal = total + (tota - 1)
    elif tota ==0 and total != 0:
        fulltotal = (total - 1) + tota
    else:
        fulltotal = total + tota

    context ={
        'beatcart':beatcart,
        'albumcart':albumcart,
        'total':total,
        'tota':tota,
        'fulltotal':fulltotal,
        'apple_url':apple_url,
    }

    return context

def remove_item(request):
    url = request.META.get('HTTP_REFERER')
    try:
        # if the item in the cart is just a beat
        deletebeat = request.POST['deletecart']
        Beatscart.objects.filter(pk=deletebeat).delete()
    except:
        # if the item in the cart is an album
        cartdelete = request.POST['cartdelete']
        Albumcart.objects.filter(pk=cartdelete).delete()

    return redirect (url)


def checkout(request):
    beatcart= Beatscart.objects.filter(user__username = request.user.username, item_paid=False)
    albumcart= Albumcart.objects.filter(user__username = request.user.username, item_paid=False)
    checkout = CheckoutForm(instance=request.user)


    #################### calculation of the items in the cart #############################
    total= 0
    tota= 0
    for item in beatcart:
        if item.beat:
            total += item.beat.price + item.quantity
        else:
            total == 0
    
    for item in albumcart:
        if item.album:
            tota += item.album.price + item.quantity
        else:
            tota == 0
    
    if total and tota != 0:
        fulltotal = (total - 1) + (tota - 1)
    elif total ==0 and tota != 0:
        fulltotal = total + (tota - 1)
    elif tota ==0 and total != 0:
        fulltotal = (total - 1) + tota
    else:
        fulltotal = total + tota

    ################### conversion to dollar ############################
    fulltotal_in_dollar = 443.63 / float(fulltotal)
    ############## end of calculation of the items in the cart ##################

    ################# Registration form for a guest user #######################
    if request.method == 'POST':
        checkout = CheckoutForm(request.POST, instance=request.user)
        if checkout.is_valid():
            fullname = checkout.cleaned_data['fullname']
            email = checkout.cleaned_data['email']
            d= checkout.save(commit=False)
            e = Checkout(fullname=fullname, email=email)
            e.save()
            messages.success(request, 'successfully registered')
            return redirect('checkout')
        else:
            messages.error(request, 'form not submitted')
            return redirect('checkout')

    ################# END Registration form for a guest user #######################
        

    ####################### PAYPAL  ###########################
    host = request.get_host()
    total = float(fulltotal_in_dollar)

    for item in beatcart:
        if item:
            item_name = item.beat
   
    for item in albumcart:
        if item:
            item_name = item.album
    

    paypal_dict ={
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        'amount': f'{total}',
        'item_name': f'{item_name}',
        'invoice': str(uuid.uuid4()),
        'currency_code': 'USD',
        'notify_url': f'http//{host}{reverse("paypal-ipn")}',
        'return_url': f'http//{host}{reverse("cback")}',
        'cancel_return': f'http//{host}{reverse("cancel")}',  
    }



    form = PayPalPaymentsForm(initial = paypal_dict)

    if form is True:
        beatcart= Beatscart.objects.filter(user__username = request.user.username, item_paid=False)
        albumcart= Albumcart.objects.filter(user__username = request.user.username, item_paid=False)
        cartup = User.objects.get(username= request.user.username)
        order_num = cartup.pk
        # take record of transaction made in paypal
        paidorder = Paidorder()
        paidorder.user = cartup
        paidorder.total = print(list(paypal_dict.values())[1])
        paidorder.cart_no = order_num
        paidorder.payment_code = print(list(paypal_dict.values())[3])
        paidorder.paid_item =True
        paidorder.firstname = cartup.first_name or cartup.username
        paidorder.save()


        ship =Ship()
        ship.user = cartup
        if beatcart:
            for item in beatcart:
                ship.beat = item.beat
        elif albumcart:
            for item in albumcart:
                ship.album = item.album

        ship.total = total
        ship.ordr_no = order_num
        ship.itm_paid =True
        ship.firstname = cartup.first_name or cartup.username
        ship.save()

   ################# END OF PAYPAL ####################### 


    context ={
        'total':total,
        'tota':tota,
        'fulltotal':fulltotal,
        'beatcart':beatcart,
        'albumcart':albumcart,
        'checkout':checkout,
        'form':form,
        'fulltotal_in_dollar':fulltotal_in_dollar,
    }

    return render(request, 'payment/checkout.html', context)


@allow_guest_user
def paidorder(request):
    if request.method == 'POST':
        if request.POST.get('paystack') == 'paystack':
            api_key= 'sk_live_3bbf1d80049d6260ef22e10a8f973b908d7a93f2'
            curl= 'https://api.paystack.co/transaction/initialize'
            cburl = 'http://127.0.0.1:8000/thankyou'
            ref_num = str(uuid.uuid4())
            total = float(request.POST['get_total'])*100
            try:
                beat_name = request.POST['get_beat']
            except:
                album_name = request.POST['get_album']

            
            beatcart= Beatscart.objects.filter(user__username = request.user.username, item_paid=False)
            albumcart= Albumcart.objects.filter(user__username = request.user.username, item_paid=False)
            cartup = User.objects.get(username= request.user.username)
            order_num = cartup.pk
            

            # out = Checkout.objects.get()
            if cartup.email == '':
                email = 'guest@gmail.com'
            else:
                email = cartup.email

            headers= {'Authorization': f'Bearer {api_key}'}
            data = {'reference':ref_num, 'order_number':order_num, 'amount': int(total), 'callback_url': cburl, 'email':email, 'currency':'NGN'}



            try:
                r = requests.post(curl, headers=headers, json=data)
            except Exception:
                messages.error(request, 'Please refresh and try again, issue being resolved')
            else:
                transback = json.loads(r.text)
                rd_url = transback['data']['authorization_url']


                # take record of transaction made
                paidorder = Paidorder()
                paidorder.user = cartup
                paidorder.total = total/100
                paidorder.cart_no = order_num
                paidorder.payment_code = ref_num
                paidorder.paid_item =True
                paidorder.firstname = cartup.first_name or cartup.username
                # paidorder.name_on_crd = user.first_name and user.last_name
                paidorder.save()


                ship =Ship()
                ship.user = cartup
                if beatcart:
                    for item in beatcart:
                        ship.beat = item.beat
                elif albumcart:
                    for item in albumcart:
                        ship.album = item.album

                ship.things_bought = beat_name or album_name
                ship.total = total/100
                ship.ordr_no = order_num
                ship.itm_paid =True
                ship.firstname = cartup.first_name or cartup.username
                ship.save()

                return redirect(rd_url)
        
        return redirect('checkout')




def cback(request):

    return redirect('thankyou')


def cancel(request):
    messages.error(request, 'Please refresh and try again, issue being resolved')
    return redirect('checkout')


def thankyou(request):
    beatcart= Beatscart.objects.filter(user__username = request.user.username, item_paid=False)
    albumcart= Albumcart.objects.filter(user__username = request.user.username, item_paid=False)

    for item in beatcart:
        item.item_paid = True
        item.save()


    for item in albumcart:
        item.item_paid = True
        item.save()

    return render(request, 'payment/thankyou.html')