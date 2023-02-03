from django.contrib import admin
from .models import Category,Item
from django_summernote.admin import SummernoteModelAdmin


admin.site.register(Category) 

class Itemslist(SummernoteModelAdmin):
    list_display = ('name','cost','image_tag','category')
    summernote_fields = ('details',)

    search_fields = (
        "name",
        "cost"
    )
admin.site.register(Item,Itemslist) 
