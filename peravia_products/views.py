from django.http import Http404
from django.views.generic import ListView, DetailView
from .models import Product, Category, MainCategory

# ----------------------------------------------------------


class ProductDetailView(DetailView):
    template_name = 'products/ProductDetail.html'
    context_object_name = 'product'

    def get_object(self, queryset=None):
        pk = self.kwargs.get('product_id')
        product = Product.objects.get(pk=pk, is_active=True)
        if product is None:
            raise Http404('Product not found')
        return product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get('product_id')
        product = Product.objects.get(pk=pk, is_active=True)
        slug = self.kwargs.get('slug').upper()
        context['page_name'] = product.title
        context['title'] = "Peravia | %s" % slug
        context['persian_page_name'] = product.persian_title
        return context


# ----------------------------------------------------------
class ProductsByCategory(ListView):
    template_name = 'products/ProductList.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = self.kwargs.get('category_name')
        category_obj = Category.objects.get(title__iexact=category)
        # main_cat = self.kwargs.get('maincategory')
        # context['previous_page'] = main_cat
        context['page_name'] = category
        context['title'] = 'Peravia | %s' % category
        context['persian_page_name'] = category_obj.persian_title
        context['persian_title'] = 'پراویا | %s' % category_obj.persian_title

        return context

    def get_queryset(self):
        category_name = self.kwargs.get('category_name').replace('-', ' ')
        category = Category.objects.get(title__iexact=category_name)
        if category is None:
            raise Http404('Not found')
        return Product.objects.get_products_by_category(category_name=category_name)

# ----------------------------------------------------------


class SubCategoryList(ListView):
    template_name = 'products/SubCategoryList.html'
    context_object_name = 'categories'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        main_category = self.kwargs.get('main_category')
        main_category_obj = MainCategory.objects.get(title__iexact=main_category)
        context['page_name'] = main_category
        context['persian_page_name'] = main_category_obj.persian_title
        context['title'] = 'Peravia | %s' % main_category
        context['persian_title'] = 'پراویا | %s' % main_category_obj.persian_title
        return context
    
    def get_queryset(self):
        main_category_name = self.kwargs.get('main_category')
        main_category = MainCategory.objects.get(title__iexact=main_category_name)
        if main_category is None:
            return Http404('Not Found')
        return Category.objects.filter(main_category__title=main_category_name)
        


# ----------------------------------------------------------


class ProductSearchView(ListView):
    template_name = 'products/ProductList.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        search_context = self.request.GET.get('q')
        context['page_name'] = 'Search Product'
        context['title'] = 'Peravia | Search for %s' % search_context
        return context

    def get_queryset(self):
        request = self.request
        query = request.GET.get('q')
        product = Product.objects.search(query)
        if product is None:
            return Http404('Product not found')
        return product
