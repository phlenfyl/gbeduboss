from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms



from beats.models import Comment
from gbeduboss.models import Booking
from beatcart.models import Checkout





class SignupForm(UserCreationForm):
    username =forms.CharField(max_length=15)
    first_name =forms.CharField(max_length=250)
    last_name =forms.CharField(max_length=250)
    email =forms.CharField(max_length=50)


    class Meta:
        model = User
        fields = ['username','first_name','last_name','email', 'password1', 'password2']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment',]
        widgets ={
            'comment': forms.Textarea(attrs={'class':'form-control bg-transparent text-white px-3 w-100', 'placeholder':'write something...'}),
        }


class StudioForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['name','email','subject','date','file','phone','message']
        widgets ={
            'file': forms.FileInput(attrs={'class':'form-control py-2 text-white', 'placeholder':'upload image file' 'multiple'}),
        }


class SongForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['name','email','subject','file','phone','message']
        widgets ={
            'file': forms.FileInput(attrs={'class':'form-control py-2 text-white', 'placeholder':'upload image file' 'multiple'}),
        }


class CheckoutForm(forms.ModelForm):
    class Meta:
        model = Checkout
        fields = ['fullname','email']
        widgets ={
            'fullname': forms.TextInput(attrs={'class':"user", 'placeholder':"fullname"}),
            'email': forms.EmailInput(attrs={'class':'user mt-3', 'placeholder':'email'}),
        }   