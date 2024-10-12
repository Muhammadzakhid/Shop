from django.urls import path
from .views import ProductDetailView, ProductListView, SignUpView, SignInView, logout_view, search_views
from django.contrib.auth import views as auth_views, logout

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', SignInView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('search/', search_views, name='search_results')
]