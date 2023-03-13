from django.urls import path

from .views import *

urlpatterns = [
    path('',ZavedeinyaHome.as_view(), name='home'),
    path('addpage/', AddPage.as_view(), name='add_page'),
    path('category/<slug:cat_slug>/',ZavedeniyaCategory.as_view(),name='category'),
    path('post/<slug:post_slug>/',ShowPost.as_view(),name='post')


]