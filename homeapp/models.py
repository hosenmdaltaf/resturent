from django.db import models
from django.utils.html import mark_safe
from django.conf import settings

class Slider(models.Model):
    image=models.ImageField(upload_to='slider_img', blank=True, null=True)

class Gallery(models.Model):
    image=models.ImageField(upload_to='gallery_img', blank=True, null=True)
    title=models.CharField( max_length=20, blank=True, null=True)
    text=models.CharField(max_length=50, blank=True, null=True)

    def image_tag(self):
        if self.image != '':
            return mark_safe('<img src="%s%s" width="50" height="50" />' % (f'{settings.MEDIA_URL}', self.image))


class Review(models.Model):
    image=models.ImageField(upload_to='gallery_img', blank=True, null=True)
    name =models.CharField( max_length=20, blank=True, null=True)
    text=models.TextField(max_length=200, blank=True, null=True)

    def image_tag(self):
        if self.image != '':
            return mark_safe('<img src="%s%s" width="50" height="50" />' % (f'{settings.MEDIA_URL}', self.image))

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=200,null=True,blank=True)
    email = models.CharField(max_length=200,null=True,blank=True)
    message = models.TextField(null=True,blank=True)
    # phonenumber= models.CharField(max_length=13,null=True,blank=True)
    # product_name = models.CharField(null=True,blank=True,max_length=400)

    # def __str__(self):
    #     return str(self.name) + '------' + str(self.product_name) 

    def __str__(self):
        return str(self.name) 

class Team(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)
    job_title= models.CharField(max_length=100,null=True,blank=True)
    image=models.ImageField(upload_to='team_img', blank=True, null=True)
    # network = models.CharField(max_length=100)
    # url = models.URLField(max_length=500)

    def image_tag(self):
        if self.image != '':
            return mark_safe('<img src="%s%s" width="50" height="50" />' % (f'{settings.MEDIA_URL}', self.image))


