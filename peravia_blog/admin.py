from django.contrib import admin
from .models import BlogPost, News

# ----------------------------------------------------------


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'title', 'created_on', 'updated_on', 'draft')
    list_filter = ('draft',)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}

    class Meta:
        model = BlogPost


# ----------------------------------------------------------
class NewsAdmin(admin.ModelAdmin):
    list_display = ('__str__','title','created_on')
    search_fields = ['title','content']
    prepopulated_fields = {'slug': ('title',)}

    class Meta:
        model = News


# ----------------------------------------------------------
admin.site.register(BlogPost, ArticleAdmin)
admin.site.register(News, NewsAdmin)
