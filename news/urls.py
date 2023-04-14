from django.urls import path
from .views import AuthorList, AuthorDetail, CategoryList, CategoryDetail, NewsList, NewsDetail

urlpatterns = [
    path('authors/', AuthorList.as_view(), name='author_list'),
    path('authors/<int:pk>/', AuthorDetail.as_view(), name='author_detail'),
    path('categories/', CategoryList.as_view(), name='category_list'),
    path('categories/<int:pk>/', CategoryDetail.as_view(), name='category_detail'),
    path('news/', NewsList.as_view(), name='news_list'),
    path('news/<int:pk>/', NewsDetail.as_view(), name='news_detail'),
]
