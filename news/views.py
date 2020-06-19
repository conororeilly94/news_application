from django.shortcuts import render, get_object_or_404, redirect
from .models import News
from main.models import Main
from django.core.files.storage import FileSystemStorage

# Create your views here. ACTIONS

def news_detail(request, word):
    
    site = Main.objects.get(pk=2)
    news = News.objects.filter(name=word)

    return render(request, 'front/news_detail.html', {'news':news, 'site':site})

def news_list(request):

    news = News.objects.all()

    return render(request, 'back/news_list.html', {'news':news})

def news_add(request):
    
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

                    b = News(name=newstitle, short_txt=newstxtshort, body=newstxt, date="2020", picurl=url, pic=filename, writer="-", catname=newscat, catid=0, views=0)
                    b.save()
                    return redirect('news_list')
                
                else:
                    error = "Your File is Bigger than 5MB"
                    return render(request, 'back/error.html', {'error':error})


            else:
                error = "Your File is not Supported"
                return render(request, 'back/error.html', {'error':error})
        
        except :
            
            error = "Please Input your Image"
            return render(request, 'back/error.html', {'error':error})


    return render(request, 'back/news_add.html')