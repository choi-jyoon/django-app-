from django.urls import path
from . import views

app_name = 'order'

urlpatterns = [
    # path('', views.order_index, name='order_index'),
    path('order_detail/<int:pk>', views.order_detail, name='order_detail'),
    path('modify_cart/', views.modify_cart, name='modify_cart'),
    path('cart/', views.cart, name='cart'),
    path('cart/<int:pk>/', views.cart_delete, name='cart_delete'),
    path('cart/<int:pk>/', views.cart_update, name='cart_update'),
    
    
]