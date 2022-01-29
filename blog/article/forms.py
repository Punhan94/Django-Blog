from django import forms
from .models import Article

# from .models import Comments

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content', 'article_images']

# class CommentForm(forms.ModelForm):
#     class Meta:
#         model = Comments
#         fields = ['comment_author', 'comment']
#
#         widgets = {
#             'comment_author': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'yazari qeyd edin'}),
#             'comment': forms.Textarea(attrs={'class': 'form-control'}),
#         }













