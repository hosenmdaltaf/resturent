from django.urls import path
from . import views

app_name='categoryapp'

urlpatterns = [
    path('item/<int:pk>', views.category_item, name='category_itempage'),
    path('single_item/<int:pk>/', views.item_detail, name='item_detail'), 
    path('all_menu/', views.all_category, name='all_category'),
    path('cat_item/<int:pk>', views.category_item, name='category_item_page'),
]
 