"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import dashboard, addArticle, UpdatePostView, deletePost, meqaleGoster, meqalelerimiz, addComment
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
  path('dashboard/', dashboard, name='dashboard'),
  path('addArticle/', addArticle, name='addArticle'),
  path('deyisdir/<int:id>/', UpdatePostView, name='update_post'),
  path('delete/<int:id>/', deletePost, name='deletePost'),
  path('MeqaleGoster/<int:id>/', meqaleGoster, name='meqalegoster'),
  path('meqaleler/', meqalelerimiz, name='meqaleler'),
  path('comment/<int:id>', addComment, name='comment')
]
