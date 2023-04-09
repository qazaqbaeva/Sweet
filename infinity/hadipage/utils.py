from hadipage.models import *
from django.db.models import Count
menu = [
        {
            'title':"Связь",'url_name':'contact'
        },
]


class DataMixin:
    def get_user_context(self,**kwargs):
        context = kwargs
        cats = Category.objects.all()
        context['menu']=menu
        context['cats']=cats
        if 'cat_selected' not in context:
            context['cat_selected']=0
        return context