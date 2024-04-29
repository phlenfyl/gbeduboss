import uuid
from django.contrib.sessions.models import Session

from beatcart.models import Beatscart, Albumcart
from guest_user.decorators import allow_guest_user




def cartpros(request):
    carty= Beatscart.objects.filter(user__username = request.user.username, item_paid=False)
    cartyl= Albumcart.objects.filter(user__username = request.user.username, item_paid=False)

    cartcount = 0
    cartcounts = 0
    
    for item in carty:
        if item:
            cartcount += item.quantity
        else:
            cartcount = 0

    for item in cartyl:
        if item:
            cartcounts += item.quantity
        else:
            cartcounts = 0
    
    count_toal =cartcounts + cartcount

    
    
    context ={
        'cartcount':cartcount,
        'cartcounts':cartcounts,
        'count_toal':count_toal,
    }

    return context


# def cart(request):
#     real_cart= Beatscart.objects.filter(user__username = request.user.username, item_paid=False)

#     total= 0
#     tota= 0
#     for item in real_cart:
#         try:
#             if item.beat:
#                 total += item.beat.price + item.quantity
#             else:
#                 total == 0
            
#             if item.album:
#                 tota += item.album.price + item.quantity
#             else:
#                 tota == 0
#         except:
#             if item.album:
#                 tota += item.album.price + item.quantity
#             else:
#                 tota == 0


#     fulltotal = total + tota
#     context ={
#         'real_cart':real_cart,
#         'total':total,
#         'tota':tota,
#         'fulltotal':fulltotal,
#     }

    # return context 


# def remove_item(request):
#     deletebeat = request.POST['deletecart']
#     Beatscart.objects.filter(pk=deletebeat).delete()
#     return deletebeat