from django.http import HttpResponse
from django.shortcuts import render,redirect
from mycolab.models import *

def show_about_page(request):
    name = 'Ramesh'
    link = 'https://www.Ramesh.com' 
    data = {
        'name':[name,'aaa'],
        'link':link
    }
    return render(request, "about.html",data)

def show_home_page(request):

    cats = Category.objects.all()
    images = Image.objects.all()

    data = {'images': images, 'cats': cats}





    return render(request,"home.html",data) 


def show_category_page(request, cid):
    print(cid)
    cats = Category.objects.all()

    category = Category.objects.get(pk=cid)

    images = Image.objects.filter(cat=category)
    data = {'images': images, 'cats': cats}

    return render(request, "home.html", data)

def home(request):
	return redirect('/home')

def search(request):
	qur = request.GET.get('search')

	cats = Category.objects.all()
	images = Image.objects.filter(title__contains = qur)
	data = {'images': images, 'cats': cats}

	return render(request, "home.html", data)



