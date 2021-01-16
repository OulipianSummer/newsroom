from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Article, Section, Author
import datetime
from django.db.models import Q

# Create your views here.

class ArticleList(ListView):
    model = Article
    template_name = 'article_list.html'
    querySet = Article.objects.all().order_by('timestamp')[:20]


class ArticleDetail(DetailView):
    model = Article
    template_name = 'article_detail.html'


class SearchResults(ListView):
    model = Article
    template_name = 'search.html'

    # A search tree that finds article titles, section names, or authors from a given query
    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Article.objects.filter(
            Q(title__icontains=query) 
            | Q(author__in=Author.objects.filter(
                Q(first_name__icontains=query) 
                | Q(last_name__icontains=query) 
                | Q(full_name__icontains=query)
            ))
            | Q(section__in=Section.objects.filter(
                Q(name__icontains=query)
            )) 
        )
        return object_list


    
