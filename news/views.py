from django.shortcuts import render, get_object_or_404, redirect
from .models import News
from main.models import Main
from django.core.files.storage import FileSystemStorage
import datetime

# Create your views here. ACTIONS

def news_detail(request, word):
    
    site = Main.objects.get(pk=2)
    news = News.objects.filter(name=word)

    return render(request, 'front/news_detail.html', {'news':news, 'site':site})

def news_list(request):

    news = News.objects.all()

    return render(request, 'back/news_list.html', {'news':news})

def news_add(request):

    
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

        newstitle = request.POST.get('newstitle')
        newscat = request.POST.get('newscat')
        newstxtshort = request.POST.get('newstxtshort')
        newstxt = request.POST.get('newstxt')


        if newstitle == "" or newstxtshort == "" or newstxt == "" or newscat == "":
            error = "All Fields are Required"
            return render(request, 'back/error.html', {'error': error})


        try:

            myfile = request.FILES['myfile']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            url = fs.url(filename)

            if str(myfile.content_type).startswith('image'):

                if myfile.size < 5000000 :

                    b = News(name=newstitle, short_txt=newstxtshort, body=newstxt, date=today, picurl=url, pic=filename, writer="-", catname=newscat, catid=0, views=0, time=time)
                    b.save()
                    return redirect('news_list')
                
                else:

                    fs = FileSystemStorage()
                    fs.delete(filename)

                    error = "Your File is Bigger than 5MB"
                    return render(request, 'back/error.html', {'error':error})


            else:

                fs = FileSystemStorage()
                fs.delete(filename)

                error = "Your File is not Supported"
                return render(request, 'back/error.html', {'error':error})
        
        except :
            
            error = "Please Input your Image"
            return render(request, 'back/error.html', {'error':error})


    return render(request, 'back/news_add.html')


def news_delete(request, pk):

    try:

        b = News.objects.get(pk=pk)

        fs = FileSystemStorage()
        fs.delete(b.pic)

        b.delete()

    except:

        error = "Something Went Wrong"
        return render(request, 'back/error.html', {'error':error})


    return redirect('news_list')