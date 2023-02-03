from django.db import models
from django.utils.html import mark_safe
from django.conf import settings

class Category(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)
    image=models.ImageField(upload_to='category_img', blank=True, null=True)

    def __str__(self):
        return str(self.name) 


class Item(models.Model):
    name = models.CharField(max_length=100)
    category =models.ForeignKey(Category,on_delete=models.CASCADE,null=True,blank=True)
    image=models.ImageField(upload_to='services_img', blank=True, null=True)
    cost =models.IntegerField(blank=True, null=True)
    details= models.TextField(default="service details",blank=True, null=True)

    def __str__(self): 
        return str(self.name) 
    
    def image_tag(self):
        if self.image != '':
            return mark_safe('<img src="%s%s" width="50" height="50" />' % (f'{settings.MEDIA_URL}', self.image))

