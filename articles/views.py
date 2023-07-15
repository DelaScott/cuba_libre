from django.shortcuts import render, get_object_or_404
from .models import Article
 

# Create your views here.
def articles_list(request):
    articles=Article.objects.all()
    return render(request, 'articles/articles_list.html', {'articles':articles})

def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    context = {
        'article': article
    }
    return render(request, 'articles/article_detail.html', context)