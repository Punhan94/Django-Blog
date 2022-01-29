from django.shortcuts import render, HttpResponse, redirect
from .forms import ArticleForm
# from .forms import CommentForm
from .models import Article, Comments
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'index.html')


@login_required(login_url='/user/login/')
def addArticle(request):
    form = ArticleForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        # title = form.cleaned_data.get("title")
        # content = form.cleaned_data.get('content')
        # new_article = Article(content=content, title=title, author_id=request.user.id)
        # new_article.save()
        article = form.save(commit=False)
        article.author = request.user
        article.save()
        messages.success(request, 'meqaleniz ugurla qeyd olundu')
        return redirect(dashboard)
    context = {'form': form}
    return render(request, 'addArticle.html', context=context)


@login_required(login_url='/user/login/')
def dashboard(request):
    form = Article.objects.filter(author=request.user)
    context = {'form': form}
    return render(request, 'dashboard.html', context=context)

@login_required(login_url='/user/login/')
def UpdatePostView(request, id):
    instance = Article.objects.get(id=id)
    form = ArticleForm(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
        form.save()
        return redirect(dashboard)
    context = {'form': form}
    return render(request, 'deyisdir.html', context=context)

@login_required(login_url='/user/login/')
def deletePost(request, id):
        Article.objects.filter(id=id).delete()
        return redirect(dashboard)

# def meqaleGoster(request, id):
#     form = get_object_or_404(Article, id=id)
#     form1 = CommentForm()
#     comments = Comments.objects.filter(article_id=id)
#     form2 = CommentForm(request.POST or None)
#     if form2.is_valid():
#         article = form2.save(commit=False)
#         article.article_id = id
#         article.save()
#         messages.success(request, 'meqaleniz ugurla qeyd olundu')
#     return render(request, 'MeqaleGoster.html', context={'form': form, 'form1': form1, 'comments': comments})

@login_required(login_url='/user/login/')
def meqaleGoster(request, id):
    form = get_object_or_404(Article, id=id)
    comments = form.comments.all()
    return render(request, 'MeqaleGoster.html', context={'form': form, 'comments': comments})

@login_required(login_url='/user/login/')
def meqalelerimiz(request):
    keyword = request.GET.get('keyword')
    if keyword:
        form = Article.objects.filter( title__contains = keyword)
        context = {'form': form}
        return render(request, 'meqaleler.html', context=context)
    form = Article.objects.all
    context = {'form': form}
    return render(request, 'meqaleler.html', context=context)

@login_required(login_url='/user/login/')
def addComment(request, id):
    article = get_object_or_404(Article, id=id)
    if request.method == 'POST':
        c_content = request.POST.get('c_content')
        new = Comments(comment_author=request.user, comment=c_content)
        new.article = article
        new.save()
    return redirect('/articles/MeqaleGoster/'+str(id))


