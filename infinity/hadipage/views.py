from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseForbidden, HttpResponseBadRequest, HttpResponseServerError
from django.shortcuts import render, redirect

menu = ["Біз туралы", "Обзор қосу", "Кері байланыс", "Кіру", "Тіркелу"]

from .models import *

def index(request):
    posts = zavedeniya.objects.all()
    return render(request, 'hadipage/index.html', {'posts': posts, 'menu': menu, 'title': 'Главная страница'})

def about(request):
    return render(request, 'hadipage/about.html', {'title': 'О сайте'})
def contact(request):
    return render(request, 'hadipage/contact.html', {'title': 'Contact'})
def category(request):
    return render(request, 'hadipage/category.html', {'title': 'Category'})
def single(request):
    return render(request, 'hadipage/single-post.html', {'title': 'Single'})

def categories(request, cat):
    return HttpResponse(f"<h1>All places by category</h1><p>{cat}</p>")

def archive(request, year):
    if int(year) > 2022:
        return redirect('home', permanent=False)

def pageNotFound404(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
def forbiddenError403(request,exception):
    return HttpResponseForbidden('<h1>Ограничение или отсутствие доступа к материалу на странице,</h1>')
def badRequest400(request,exceprion):
    return HttpResponseBadRequest('<h1>Плохой запрос</h1>')
def serverError500(request):
    return HttpResponseServerError('<h1>Сервер столкнулся с неожиданной ошибкой</h1>')