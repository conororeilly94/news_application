from django.shortcuts import render, get_object_or_404, redirect
from .models import ContactForm
from news.models import News
from cat.models import Cat
from subcat.models import SubCat
from django.contrib.auth import authenticate, login, logout
from django.core.files.storage import FileSystemStorage
import datetime

# Create your views here. ACTIONS


def contact_add(request):

    now = datetime.datetime.now()

    year = now.year
    month = now.month
    day = now.day
    hour = now.hour
    minute = now.minute

    if len(str(day)) == 1:
        day = "0" + str(day)
    if len(str(month)) == 1:
        month = "0" + str(month)

    today = str(year) + "/" + str(month) + "/" + str(day)
    time = str(hour) + ":" + str(minute)

    
    if request.method == 'POST':        

        name = request.POST.get('name')
        email = request.POST.get('email')
        txt = request.POST.get('msg')

        if name == "" or email == "" or txt == "":
            msg = "All Fields Required"
            return render(request, 'front/msgbox.html', {'msg':msg})

        b = ContactForm(name=name, email=email, txt=txt, date=today, time=time)
        b.save()
        msg = "Your Message Has Been Recieved"
        return render(request, 'front/msgbox.html', {'msg':msg})

    return render(request, 'front/msgbox.html')


def contact_show(request):

    # Login Check Start
    if not request.user.is_authenticated:
        return redirect('mylogin')
    # Login Check End

    msg = ContactForm.objects.all()

    return render(request, 'back/contact_form.html', {'msg':msg})


def contact_del(request, pk):

    # Login Check Start
    if not request.user.is_authenticated:
        return redirect('mylogin')
    # Login Check End

    b = ContactForm.objects.filter(pk=pk)
    b.delete()

    return redirect('contact_show')