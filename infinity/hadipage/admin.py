from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *

class zavedeniaAdmin(admin.ModelAdmin):
    list_display = ('id','title','content','certificate','namazhana_omov','get_html_photo','time_create','time_update','is_published')
    list_display_links = ('id','title')
    search_fields = ('title','content')
    list_editable = ('is_published',)
    list_filter = ('is_published','time_create')
    prepopulated_fields ={"slug":("title",)}
    fields = ('title','slug','category','certificate','namazhana_omov','content','photo','get_html_photo','is_published')
    readonly_fields = ('time_create','time_update','get_html_photo')
    save_on_top = True
    def get_html_photo(self,object):
        return mark_safe(f"<img src='{object.photo.url}'width=50>")
    get_html_photo.short_description = "Photo"
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    list_display_links = ('id','name')
    search_fields = ('name',)
    prepopulated_fields = {"slug":("name",)}
admin.site.register(zavedeniya,zavedeniaAdmin)
admin.site.register(Category,CategoryAdmin)

admin.site.site_title = 'Админ панель сайта iHadi'
admin.site.site_header = 'Админ панель сайта iHadi'
