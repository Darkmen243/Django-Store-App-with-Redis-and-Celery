from django.urls import include, path
from .views import ProductListCreateView, ProductDetailView, CategoryListView, CategoryDetailView, CategoryDetailManageView, CategoryManageView


urlpatterns = [
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('categories/<slug:slug>/', CategoryDetailView.as_view(), name='category-detail'),
    path('', ProductListCreateView.as_view(), name='product-list'),
    path('<slug:slug>/', ProductDetailView.as_view(), name='product-detail'),

]