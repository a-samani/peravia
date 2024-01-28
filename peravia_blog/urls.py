from django.urls import path
from .views import PostList, PostDetail, NewsList, NewsDetail,ArticleSearch

app_name = 'blog'

urlpatterns = [
    path('article', PostList.as_view(), name='article_list'),
    path('article/<int:post_id>/<str:slug>',
         PostDetail.as_view(), name='article_detail'),
    path('search', ArticleSearch.as_view(), name='article_search'),
    path('news', NewsList.as_view(), name='news_list'),
    path('news/<int:news_id>/<str:slug>',
         NewsDetail.as_view(), name='news_detail'),
]
