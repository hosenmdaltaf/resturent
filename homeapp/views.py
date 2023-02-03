from django.shortcuts import render

from homeapp.models import Slider,Review,Gallery,Contact,Team
from categoryapp.models import Category
from django.contrib import messages

def homepage(request):
    sliders = Slider.objects.all()
    categories = Category.objects.all()
    galleries = Gallery.objects.all()[:7]
    if request.method == "POST":
        try:
            name = request.POST.get("name")
            email = request.POST.get("email")
            message = request.POST.get("message") 
            Contact.objects.create(name=name,message=message,email=email)
#             msg = f"""
#             name: {name}.
# email: {email}.
# phonenumber: {phonenumber}. 
# message: {message}.
#             """
#             receiver = '018808717'
#             sms_send = smsapi(msg,receiver)
            return render(request,'global/thankyou.html')
        except:
            messages.warning(request, 'Please fill up all the form feild currectly!')
    context={
        'sliders':sliders,
        'categories':categories,
        'galleries':galleries,
    }
    return render(request,'homeapp/index.html',context)


def aboutus(request):
    teams = Team.objects.all()
    return render(request,'homeapp/aboutus.html',{'teams':teams}) 

# def gallery(request):
#     gallerys=Gallery.objects.all()
#     # servicecart = Tour.objects.all()[:4] 
#     return render(request,'categoryapp/gallery.html',{'gallerys':gallerys})


def contact(request):
    if request.method == "POST":
        try:
            name = request.POST.get("name")
            email = request.POST.get("email")
            message = request.POST.get("message") 
            Contact.objects.create(name=name,message=message,email=email)
#             msg = f"""
#             name: {name}.
# email: {email}.
# phonenumber: {phonenumber}. 
# message: {message}.
#             """
#             receiver = '018808717'
#             sms_send = smsapi(msg,receiver)
            return render(request,'global/thankyou.html')
        except:
            messages.warning(request, 'Please fill up all the form feild currectly!')
    return render(request,'homeapp/contact.html')

