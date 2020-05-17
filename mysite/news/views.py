from django.shortcuts import render
from .models import Article

def article_archive(request):
    a_list = Article.objects.order_by('-pub_date')
    context = {'article_list' : a_list}
    return render(request, 'news/article_archive.html',context)

def year_archive(request, year):
    a_list = Article.objects.filter(pub_date__year=year)
    context = {'year': year, 'article_list': a_list}
    return render(request, 'news/year_archive.html', context)

def month_archive(request, year, month):
    a_list = Article.objects.filter(pub_date__year=year, pub_date__month=month)
    context = {'year': year, 'month': month, 'article_list': a_list}
    return render(request, 'news/month_archive.html', context) 

def article_detail(request, year, month, pk):
    a_list = Article.objects.filter(pub_date__year=year, pub_date__month=month, pk = pk)
    context = {'year': year, 'month': month, 'article_list': a_list}
    return render(request, 'news/aritcle_detail.html', context)
