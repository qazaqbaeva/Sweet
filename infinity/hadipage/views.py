from urllib import request

from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseForbidden, HttpResponseBadRequest, HttpResponseServerError
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from .forms import *

menu = [
        {},
]
#{'title': "О сайте", 'url_name': 'about'},
#        {'title': "Обратная связь", 'url_name': 'contact'},
#     {'title': "Войти", 'url_name': 'login'
from .models import *

class ZavedeinyaHome(ListView):
    model = zavedeniya
    template_name = 'hadipage/index.html'
    context_object_name = 'posts'


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu']=menu
        context['title']='Главная страница'
        context['cat_selected']=0
        return context

    def get_queryset(self):
        return zavedeniya.objects.filter(is_published=True)



# def index(request):
#     posts = zavedeniya.objects.all()
#
#     context = {
#         'posts': posts,
#         'menu': menu,
#         'title': 'Главная страница',
#         'cat_selected': 0,
#     }
#
#     return render(request, 'hadipage/index.html', context=context)

class ShowPost(DetailView):
    model = zavedeniya
    template_name = 'zavedeniya/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['title']=context['post']
        context['menu']=menu
        return context



# def show_post(request,post_slug):
#     post=get_object_or_404(zavedeniya,slug=post_slug)
#     context = {
#         'post': post,
#         'menu': menu,
#         'title':post.title,
#         'cat_selected':post.category_id,
#     }
#     return render(request, 'hadipage/post.html', context=context)

class ZavedeniyaCategory(ListView):
    model = zavedeniya
    template_name = 'zavedeniya/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        return zavedeniya.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title']='Категория -' + str(context['posts'][0].cat)
        context['menu']=menu
        context['cat_selected']=context['posts'][0].cat_id
        return context

class AddPage(CreateView):
    form_class = AddPostForm
    template_name = 'zavedeniya/addpage.html'
    success_url = reverse_lazy('home')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title']='Create post'
        context['menu']=menu
        return context
# def addpage(request):
#     if request.method =='POST':
#         form = AddPostForm(request.POST)
#         if form.is_valid():
#             try:
#                 zavedeniya.objects.create(**form.cleaned_data)
#                 return redirect('home')
#             except:
#                 form.add_error(None, 'Ошибка добавления поста')
#     else:
#         form = AddPostForm()
#     return render(request,'hadipage/addpage.html', {'form': form, 'menu': menu, 'title' : 'Добавление статьи'})

def pageNotFound404(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
def forbiddenError403(request,exception):
    return HttpResponseForbidden('<h1>Ограничение или отсутствие доступа к материалу на странице,</h1>')
def badRequest400(request,exceprion):
    return HttpResponseBadRequest('<h1>Плохой запрос</h1>')
def serverError500(request):
    return HttpResponseServerError('<h1>Сервер столкнулся с неожиданной ошибкой</h1>')


# def show_category(request, cat_id):
#     posts = zavedeniya.objects.filter(category_id=cat_id)
#
#     if len(posts)==0:
#         raise Http404()
#     context = {
#         'posts': posts,
#         'menu': menu,
#         'title': 'Отображение по категориям',
#         'cat_selected': 0,
#     }
#
#     return render(request, 'hadipage/index.html', context=context)