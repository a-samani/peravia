from multiprocessing import context
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import BlogPost, News
from django.http import Http404


# ----------------------------------------------------------
class PostList(ListView):
    template_name = 'posts/BlogPosts.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        return BlogPost.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_name'] = "Article"
        context['title'] = "پراویا | مقالات" if self.request.LANGUAGE_CODE == 'fa' else "Peravia | article"
        context['persian_page_name'] = "مقالات"
        context['persian_title'] = "پراویا | مقالات"
        return context


# ----------------------------------------------------------
class PostDetail(DetailView):
    template_name = 'posts/PostDetail.html'
    context_object_name = 'post'

    def get_object(self, queryset=None):
        pk = self.kwargs.get('post_id')
        post = BlogPost.objects.get(pk=pk)
        if post is None:
            return Http404('Post not found')
        return post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        title = self.kwargs.get('slug').replace('-', ' ')
        context['latest_article'] = BlogPost.objects.all()[:3]
        context['page_name'] = 'Article'
        context['title'] = "Peravia | %s" % title
        return context
# ----------------------------------------------------------
class ArticleSearch(ListView):
    template_name = 'posts/BlogPosts.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self) :
        req = self.request
        query = req.GET.get('search')
        articles = BlogPost.objects.serach_article(query)
        if articles is None:
            return Http404('Article not found')
        return articles
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        search = self.request.GET.get('search')
        context['page_name'] = 'Search Article'
        context['title'] = "Peravia | %s" % search
        return context

# ----------------------------------------------------------
class NewsList(ListView):
    template_name = 'news/NewsList.html'
    context_object_name = "newslist"
    paginate_by = 5

    def get_queryset(self):
        return News.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_name'] = "News"
        context['title'] = "پراویا | اخبار" if self.request.LANGUAGE_CODE == 'fa' else "Peravia | News"
        context['persian_page_name'] = "اخبار"
        context['persian_title'] = "پراویا | اخبار"
        return context

# ----------------------------------------------------------


class NewsDetail(DetailView):
    template_name = 'news/NewsDetail.html'
    context_object_name = 'news'

    def get_object(self, queryset=None):
        pk = self.kwargs.get('news_id')
        news = News.objects.get(pk=pk)
        if news is None:
            return Http404('News not found')
        return news

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        title = self.kwargs.get('slug').replace('-', ' ')
        context['latest_news'] = News.objects.all()[:3]
        context['page_name'] = "News"
        context['title'] = "Peravia | %s" % title
        return context
