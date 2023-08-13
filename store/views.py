from django.shortcuts import redirect, render
from django.views.generic import ListView, DetailView
from .models import Product, ShoppingCart, ShoppingCartItem
from django.contrib import messages
from django.utils import timezone
from django.shortcuts import get_object_or_404


class ProductListView(ListView):
    model = Product
    template_name = 'store/product_list.html'
    ordering = ['name']
    paginate_by = 10


class ProductDetailView(DetailView):
    model = Product
    template_name = 'store/product_detail.html'
    context_object_name = 'product'
    # context_object_name = 'products'
    ordering = ['name']
    paginate_by = 10


def Addtocart(request, id):
    shopping_cart = ShoppingCart.objects.get_or_create(
        customer=request.user,
    )
    shopping_cart_item = ShoppingCartItem.objects.create(
        cart=shopping_cart[0],
        product=Product.objects.get(id=id),
        quantity=request.POST.get('quantity'),
        price=request.POST.get('price'),
    )
    shopping_cart_item.save()
    messages.info(request, "This item was added to your cart.")
    return redirect("shopping-cart-list")


class Shopping_Cart_List(ListView):
    model = ShoppingCartItem
    template_name = 'store/shopping_cart.html'
    context_object_name = 'shopping_cart_items'
    ordering = ['product__name']
    paginate_by = 10

    def get_queryset(self):
        return ShoppingCartItem.objects.filter(
            cart__customer=self.request.user)


def update_item(request, item_id):
    item = get_object_or_404(ShoppingCartItem, id=item_id)

    if request.method == 'POST':
        # Update the item based on POST data.
        # You might want a form to validate the changes.
        # Assuming there's a field 'quantity' that might be updated:
        new_quantity = request.POST.get('quantity')
        item.quantity = new_quantity
        item.save()
        return redirect('shopping_cart')  # Assuming the name of the view that displays the cart is 'shopping_cart'

    return render(request, 'update_item.html', {'item': item})


def increase_quantity(request, item_id):
    item = get_object_or_404(ShoppingCartItem, id=item_id)
    item.quantity += 1
    item.save()
    return redirect('shopping_cart')  # Redirect back to the shopping cart after increasing quantity


def delete_item(request, item_id):
    item = get_object_or_404(ShoppingCartItem, id=item_id)

    if request.method == 'POST':
        item.delete()
        return redirect('shopping_cart')

    return render(request, 'confirm_delete.html', {'item': item})
