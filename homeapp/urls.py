from django.urls import path
from . import views

app_name='homeapp'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('aboutus/', views.aboutus, name='aboutus'), 
    path('contact/', views.contact, name='contact'), 
    # path('hotel_list/', views.all_hotels, name='all_hotels'),
    # path('category/<int:pk>', views.category_hotel, name='category_hotelpage'),
    # path('hotel/<int:pk>/', views.hotel_detail, name='hotel_detail'),
    # # path('about/', views.about, name='aboutpage'),
    # path('gallery/', views.gallery, name='gallerypage'),
    # # path('category/<int:pk>', views.category_hotel, name='category_hotelpage'),
    # path('all_visa/', views.all_visa, name='visa_page'),
    # path('visa/<int:pk>', views.visa_detail, name='visa_detailpage'),

]