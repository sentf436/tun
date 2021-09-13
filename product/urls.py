from django.urls import path

from product.views import ProductListCreateView, ProductDetailRetrieveUpdateDestroyView, CategoryListCreateView, CategoryDetailCreateView

urlpatterns = [
    path('all/', ProductListCreateView().as_view(), name='product-list'),
    path('category/', CategoryListCreateView().as_view(), name='category-list'),
    path('category/<pk>', CategoryDetailCreateView.as_view(), name='category-detail'),
    path('all/<int:pk>', ProductDetailRetrieveUpdateDestroyView.as_view(), name='product-detail'),
]