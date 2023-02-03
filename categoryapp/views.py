from django.shortcuts import render
from categoryapp.models import Category,Item
from django.contrib import messages
from homeapp.models import Contact
# from bookingapp.sms import smsapi

# def category_tour(request,pk): 
#     category_tours = Tour.objects.filter(category=pk)
#     categorys = Category_tour.objects.all()
#     return render(request,'categoryapp/tour_category.html',{'category_tours':category_tours,'categorys':categorys})

def all_category(request):
    categories = Category.objects.all()
    return render(request,'categoryapp/all_menu.html',{'categories':categories}) 

def category_item(request,pk): 
    items = Item.objects.filter(category=pk)
    print('Data---------')
    print(items)
    return render(request,'categoryapp/item_list_cat.html',{'items': items })


def item_detail(request,pk):
    object= Item.objects.get(pk=pk)
#     eventscart = Events.objects.all()[:4]
#     if request.method == "POST":
#         try:
#             name = request.POST.get("name")
#             email = request.POST.get("email")
#             message = request.POST.get("message") 
#             phonenumber = request.POST.get("phonenumber")
#             product_name = request.POST.get("Servicesname")  
#             Contact.objects.create(name=name,message=message,phonenumber=phonenumber,
#             email=email,product_name=product_name)
#             msg = f"""
#             name: {name}.
# email: {email}.
# phonenumber: {phonenumber}. 
# Booked_Package: {product_name}.
# message: {message}.
#             """
#             receiver = '01880871297'
#             sms_send = smsapi(msg,receiver)
#             return render(request,'global/thankyou.html')
#         except:
#             messages.warning(request, 'Please fill up all the form feild currectly!')
    return render(request,'categoryapp/item_details.html',{'object':object})

