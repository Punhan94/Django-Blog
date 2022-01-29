from django.db import models
from ckeditor.fields import RichTextField
from django import forms
from django.contrib import auth
# Create your models here.

class Article(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = RichTextField()
    article_images = models.FileField( blank=True, null=True, verbose_name='Sekil elave edin')
    created_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title

class Comments(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name='Meqale', related_name='comments')
    comment_author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    comment = models.TextField(verbose_name='Serhinizi bildirin')

