from django.urls import path
from .views import ProductListView, ProductDetailView, Addtocart, Shopping_Cart_List, update_item, increase_quantity, delete_item

urlpatterns = [
    path('products/', ProductListView.as_view(),
         name='product-list'),
    path('products/<int:pk>/', ProductDetailView.as_view(),
         name='product-detail'),
    path('products/<int:id>/addtocart/', Addtocart,
         name='add-to-cart'),
    path('shopping-cart/', Shopping_Cart_List.as_view(),
         name='shopping-cart-list'),
    path('shopping-cart/update/<int:item_id>/', update_item,
         name='update_item'),
    path('shopping-cart/increase/<int:item_id>/', increase_quantity,
         name='increase_quantity'),
    path('shopping-cart/delete/<int:item_id>/', delete_item,
         name='delete_item'),

]
