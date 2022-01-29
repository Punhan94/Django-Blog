from django.contrib import admin

from .models import Article
from .models import Comments

# Register your models here.

#admin.site.register(Article)

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    class Meta: model = Article
    list_display = ['title', 'author']
    list_display_links = ['title']
    search_fields = ['title']
    list_filter = ['title']

@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    class Meta: model = Comments
    list_display = ['comment_author', 'comment']


