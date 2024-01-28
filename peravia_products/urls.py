from django.urls import path
from .views import *

# ----------------------------------------------------------
app_name = 'product'
# ----------------------------------------------------------
urlpatterns = [
    path('<int:product_id>/<str:slug>', ProductDetailView.as_view(), name='single_product'),
    path('search', ProductSearchView.as_view(), name='product_search'),
    path('<str:main_category>', SubCategoryList.as_view(), name="sub_category_list"),
    path('search/<str:category_name>', ProductsByCategory.as_view(), name='product_by_category'),
]
