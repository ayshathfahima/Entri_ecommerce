from . import views
from django.urls import path

urlpatterns = [
    path('',views.allproducts, name='allproducts'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('signout/', views.signout, name='signout'),


    path('<slug:slug_c>/', views.allproducts, name='product_by_category'),
    path('<slug:slug_c>/<slug_p>/', views.prod_det, name='product_catdetail'),





]
