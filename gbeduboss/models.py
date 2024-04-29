from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Banner(models.Model):
    first_word = models.CharField(max_length=200, blank=True, null=True)
    second_word = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.first_word
    
    class Meta:
        db_table = 'banner'
        managed = True
        verbose_name = 'Banner'
        verbose_name_plural = 'Banners'



# second content
class Services(models.Model):
    header_one = models.CharField(max_length=50, blank=True, null=True)
    small_header= models.CharField(max_length=50, blank=True, null=True)
    service_image = models.ImageField(upload_to = 'services_pics', default='phone.jpg', blank=True, null=True)

    def __str__(self):
        return self.header_one


class Subname(models.Model):
    name = models.CharField(max_length=20, blank=True,null=True)

    def __str__(self):
        return self.name

class Subdescription(models.Model):
    owned_by= models.ForeignKey(Subname, on_delete=models.CASCADE)
    description = models.TextField(blank=True,null=True)
    one = models.BooleanField()
    two = models.BooleanField()
    three = models.BooleanField()
    four = models.BooleanField()
    five = models.BooleanField()
    six = models.BooleanField()

    def __str__(self):
        return self.owned_by.name
    
    class Meta:
        db_table = 'subdescription'
        managed = True
        verbose_name = 'Subdescription'
        verbose_name_plural = 'Subdescriptions'

# second content end

# Third and Forth Content
class Advert(models.Model):
    third_header= models.CharField(max_length=100, blank=True,null=True)
    third_subheader= models.CharField(max_length=100, blank=True,null=True)
    link_name= models.CharField(max_length=100, blank=True,null=True)
    link_one= models.URLField(max_length=200, blank=True,null=True)
    link_nam= models.CharField(max_length=100, blank=True,null=True)
    link_two= models.URLField(max_length=200, blank=True,null=True)

    forth_header= models.CharField(max_length=100, blank=True,null=True)
    forth_subheader= models.CharField(max_length=100, blank=True,null=True)


    def __str__(self):
        return self.third_header
    
    class Meta:
        db_table = 'advert'
        managed = True
        verbose_name = 'Advert'
        verbose_name_plural = 'Adverts'

# Third and Forth Content ends


#Newsletter
class Newsletter(models.Model):
    name = models.CharField(max_length=100, blank=True,null=True)
    subname = models.CharField(max_length=100, blank=True,null=True)
    email = models.EmailField(blank=True,null=True)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'newsletter'
        managed = True
        verbose_name = 'Newsletter'
        verbose_name_plural = 'Newsletters'


class Booking(models.Model):
    name = models.CharField(max_length=100,blank=True,null=True)
    email = models.EmailField(blank=True,null=True)
    subject = models.CharField(max_length=200,blank=True,null=True)
    date = models.DateField(blank=True,null=True)
    file = models.FileField(upload_to='booking_files',blank=True,null=True)
    phone = models.CharField(max_length=100,blank=True,null=True)
    message = models.TextField(blank=True,null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return '%s - %s' % (self.name, self.subject)