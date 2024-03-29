from django.db import models
from django.urls import reverse

class zavedeniya(models.Model):
    title = models.CharField(max_length=255,verbose_name="Заголовок")
    slug=models.SlugField(max_length=255,unique=True,db_index=True,verbose_name="URL")
    content= models.TextField(blank=True)
    certificate = models.CharField(max_length=255)
    namazhana_omov=models.BooleanField(default=True)
    photo=models.ImageField(upload_to="photos/%Y/%m/%d")
    time_create=models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    category=models.ForeignKey('Category', on_delete=models.PROTECT)
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug' : self.slug})

    class Meta:
        verbose_name='Заведения'
        verbose_name_plural='Заведения'
        ordering = ['id']
class Category(models.Model):
    name=models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'category_slug': self.slug})
    class Meta:
        verbose_name='Категория'
        verbose_name_plural='Категории'
        ordering=['id']

