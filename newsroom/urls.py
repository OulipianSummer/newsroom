from django.urls import path
from . import views

urlpatterns = [
    path('', views.ArticleList.as_view(), name='article_list'),
    path('article/<slug:slug>', views.ArticleDetail.as_view(), name='article_detail'),
    path('section/<slug:slug>', views.SectionList.as_view(), name='section_list'),
    path('search/', views.SearchResults.as_view(), name='search_results')
]
