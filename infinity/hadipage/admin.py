from django.contrib import admin
from .models import *

class zavedeniaAdmin(admin.ModelAdmin):
    list_display = ('id','title','content','certificate','namazhana_omov','photo','time_create','time_update','is_published')
    list_display_links = ('id','title')
    search_fields = ('title','content')
    list_editable = ('is_published',)
    list_filter = ('is_published','time_create')
    prepopulated_fields ={"slug":("title",)}
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    list_display_links = ('id','name')
    search_fields = ('name',)
    prepopulated_fields = {"slug":("name",)}
admin.site.register(zavedeniya,zavedeniaAdmin)
admin.site.register(Category,CategoryAdmin)