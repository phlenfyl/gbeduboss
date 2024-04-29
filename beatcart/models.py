from django.db import models
from django.contrib.auth.models import User, AnonymousUser
from beats.models import *

# Create your models here.


class Albumcart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank= True, null= True)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, blank=True, null=True)
    quantity =models.IntegerField()
    beat_name = models.CharField(max_length=100)
    total = models.IntegerField(default=1)
    order_no= models.CharField(max_length=50)
    session_id= models.CharField(max_length=100, blank= True, null= True)
    item_paid = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

    class Meta:
        unique_together = ('user', 'session_id',)


class Beatscart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank= True, null= True)
    beat = models.ForeignKey(Beats, on_delete=models.CASCADE, blank=True, null=True)
    quantity =models.IntegerField()
    beat_name = models.CharField(max_length=100)
    total = models.IntegerField(default=0)
    order_no= models.CharField(max_length=50)
    session_id= models.CharField(max_length=100, blank= True, null= True)
    item_paid = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

    class Meta:
        unique_together = ('user', 'session_id',)


class Checkout(models.Model):
    fullname = models.CharField(max_length = 70, blank= True, null= True)
    email = models.EmailField(max_length=100, blank= True, null= True)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.fullname


class Paidorder(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    total = models.FloatField()
    cart_no = models.CharField(max_length=36, blank=True, null=True)
    payment_code = models.CharField(max_length=50)
    paid_item = models.BooleanField(default=False)
    firstname= models.CharField(max_length=50)


    def __str__(self):
        return self.user.username

    

class Ship(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    beat = models.ForeignKey(Beats, on_delete=models.CASCADE, blank=True, null=True)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, blank=True, null=True)
    ordr_no= models.CharField(max_length=50)
    things_bought= models.CharField(max_length=500, blank=True, null=True)
    itm_paid= models.BooleanField(default=False)
    total= models.FloatField()
    firstname= models.CharField(max_length=200,blank=True, null=True)

    def __str__(self):
        return self.user.username
