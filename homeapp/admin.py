from django.contrib import admin
from .models import Slider,Gallery,Review
from .models import Contact,Team


class Gallerylist(admin.ModelAdmin):
    list_display = ('title','image_tag','text')

class Reviewlist(admin.ModelAdmin):
    list_display = ('name','image_tag')

admin.site.register(Slider)
admin.site.register(Gallery,Gallerylist)
admin.site.register(Review,Reviewlist)


class Contactlist(admin.ModelAdmin):
    list_display = ('name', 'email')


class Teamlist(admin.ModelAdmin):
    list_display = ('name','image_tag','job_title')

admin.site.register(Contact,Contactlist)
    
admin.site.register(Team,Teamlist)

