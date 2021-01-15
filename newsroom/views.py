from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Article, Section
import datetime

# Create your views here.

class ArticleList(ListView):
    model = Article
    template_name = 'article_list.html'
    querySet = Article.objects.all().order_by('timestamp')[:20]


class ArticleDetail(DetailView):
    model = Article
    template_name = 'article_detail.html'


class SectionList(ListView):
    model = Article
    template_name = 'article_list.html'


    
