
from django.urls import path
from django.views.decorators.cache import cache_page
from .views import *

urlpatterns = [
    path('',ZavedeinyaHome.as_view(), name='home'),
    path('addpage/', addpage, name='add_page'),
    path('login/',LoginUser.as_view(),name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/',RegisterUser.as_view(),name='register'),
    path('category/<slug:category_slug>/',ZavedeniyaCategory.as_view(),name='category'),
    path('post/<slug:post_slug>/',ShowPost.as_view(),name='post'),
    path('about/', about, name='about'),
    path('contact/',ContactFormView.as_view(),name='contact')


]