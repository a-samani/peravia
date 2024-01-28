from django.contrib import admin

from .models import Product, Specification, Advantage, Category, MainCategory


# ----------------------------------------------------------
class ProductAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'title', 'application', 'is_active']
    list_editable = ['is_active',]
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['title', 'application']
    class Meta:
        model = Product

# ----------------------------------------------------------
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ['__str__', 'title']
    class Meta:
        model = Category


# ----------------------------------------------------------
admin.site.register(Product,ProductAdmin)
admin.site.register(Specification)
admin.site.register(Advantage)
admin.site.register(Category, CategoryAdmin)
admin.site.register(MainCategory)

