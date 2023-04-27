from urllib import request

from django.contrib.auth import logout, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseForbidden, HttpResponseBadRequest, HttpResponseServerError
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, FormView
from .forms import *
from .models import *
from .utils import DataMixin

menu = [
        {},
]
#{'title': "О сайте", 'url_name': 'about'},
#        {'title': "Обратная связь", 'url_name': 'contact'},
#     {'title': "Войти", 'url_name': 'login'

class ZavedeinyaHome(ListView):
    paginate_by = 4
    model = zavedeniya
    template_name = 'hadipage/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cat_selected']=0
        return context

    def get_queryset(self):
        return zavedeniya.objects.filter(is_published=True)

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     c_def=self.get_user_context(title="Main page")
    #     return dict(list(context.items())+list(c_def.items()))
    #




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
def about(request):
    contact_list = zavedeniya.objects.all()
    paginator = Paginator(contact_list,3)
    page_number=request.GET.get('page')
    page_obj=paginator.get_page(page_number)
    return render(request, 'hadipage/about.html', {'page_obj':page_obj,'menu': menu, 'title':'О сайте'})


# class ShowPost(DataMixin,DetailView):
#     model = zavedeniya
#     template_name = 'zavedeniya/post.html'
#     slug_url_kwarg = 'post_slug'
#     context_object_name = 'post'
#
#     def get_context_data(self, **kwargs):
#         context=super().get_context_data(**kwargs)
#         c_def = self.get_user_context(title=context['post'])
#         return dict(list(context.items())+list(c_def.items()))



def show_post(request,post_slug):
    post=get_object_or_404(zavedeniya,slug=post_slug)
    context = {
        'post': post,
        'menu': menu,
        'title':post.title,
        'cat_selected':post.category_id,
    }
    return render(request, 'hadipage/post.html', context=context)

class ZavedeniyaCategory(ListView):
    paginate_by = 3
    model = zavedeniya
    template_name = 'zavedeniya/index.html'
    context_object_name = 'posts'
    # allow_empty = False
    def get_queryset(self):
        return zavedeniya.objects.filter(category__slug=self.kwargs['category_slug'],is_published=True)


    # def get_queryset(self):
    #     return zavedeniya.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True)
    #
    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     c_def = self.get_user_context(title='Категория - ' + str(context['posts'][0].category),
    #                                   cat_selected=context['posts'][0].cat_id)
    #     return dict(list(context.items())+list(c_def.items()))

# class AddPage(LoginRequiredMixin,CreateView):
#     # form_class = AddPostForm
#     # template_name = 'zavedeniya/addpage.html'
#     # success_url = reverse_lazy('home')
#     # def get_context_data(self, **kwargs):
#     #     context = super().get_context_data(**kwargs)
#     #     context['title']='Create post'
#     #     context['menu']=menu
#     #     return context
def addpage(request):
    if request.method =='POST':
        form = AddPostForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AddPostForm()
    return render(request,'hadipage/addpage.html', {'form': form, 'menu': menu, 'title' : 'Добавление статьи'})

def pageNotFound404(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
def forbiddenError403(request,exception):
    return HttpResponseForbidden('<h1>Ограничение или отсутствие доступа к материалу на странице,</h1>')
def badRequest400(request,exceprion):
    return HttpResponseBadRequest('<h1>Плохой запрос</h1>')
def serverError500(request):
    return HttpResponseServerError('<h1>Сервер столкнулся с неожиданной ошибкой</h1>')

#
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
class RegisterUser(DataMixin,CreateView):
    form_class = RegisterUserForm
    template_name='hadipage/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self,*,object_list=None, **kwargs):
        context=super().get_context_data(**kwargs)
        c_def=self.get_user_context(title="Registration")
        return dict(list(context.items())+list(c_def.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'hadipage/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Авторизация")
        return dict(list(context.items()) + list(c_def.items()))
    def get_success_url(self):
        return reverse_lazy('home')
def logout_user(request):
    logout(request)
    return redirect('login')


class ContactFormView(DataMixin, FormView):
    form_class = ContactForm
    template_name = 'hadipage/contact.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Обратная связь")
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        print(form.cleaned_data)
        return redirect('home')
