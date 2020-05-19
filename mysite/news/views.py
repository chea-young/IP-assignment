from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .models import Article

class ArticleView(generic.ListView):
    model = Article
    template_name = 'news/article_archive.html'

    def get_queryset(self):
        return Article.objects.filter(pub_date__lte=timezone.now())

def year_archive(request, year):
    a_list = Article.objects.filter(pub_date__year=year)
    context = {'year': year, 'article_list': a_list}
    return render(request, 'news/year_archive.html', context)

def month_archive(request, year, month):
    a_list = Article.objects.filter(pub_date__year=year, pub_date__month=month)
    context = {'year': year, 'month': month, 'article_list': a_list}
    return render(request, 'news/month_archive.html', context) 

class DetailView(generic.DetailView):
    model = Article
    template_name = 'news/aritcle_detail.html'

"""def article_archive(request):
    a_list = Article.objects.order_by('-pub_date')
    context = {'article_list' : a_list}
    return render(request, 'news/article_archive.html',context)"""


"""class YearView(generic.ListView):
    model = Article
    template_name = 'news/year_archive.html'

class MonthView(generic.ListView):
    model = Article
    template_name = 'news/month_archive.html'"""

#def article_detail(request, year, month, pk):
    #a_list = Article.objects.filter(pub_date__year=year, pub_date__month=month, pk = pk)
    #context = {'year': year, 'month': month, 'article_list': a_list}
    #return render(request, 'news/aritcle_detail.html', context) 
