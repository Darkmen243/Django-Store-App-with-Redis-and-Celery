from django.urls import include, path
from .views import ProductListCreateView, ProductDetailView, CategoryListView, CategoryDetailView, CategoryDetailManageView, CategoryManageView


urlpatterns = [
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('categories/<slug:slug>/', CategoryDetailView.as_view(), name='category-detail'),
    
    # Admin endpoints (require admin auth)
    path('admin/categories/', CategoryManageView.as_view(), name='admin-category-list'),
    path('admin/categories/<slug:slug>/', CategoryDetailManageView.as_view(), name='admin-category-detail'),

    path('', ProductListCreateView.as_view(), name='product-list'),
    path('<slug:slug>/', ProductDetailView.as_view(), name='product-detail'),

]