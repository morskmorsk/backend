from django.db import models
from accounts.models import CustomUser as Profile
from datetime import timezone
from decimal import Decimal


class Department(models.Model):
    name = models.CharField(max_length=200)
    taxable = models.CharField(max_length=3, default='yes')

    def __str__(self):
        return self.name

    def __repr__(self):
        return '<Department object ({})>'.format(self.id)

    class Meta:
        ordering = ('id',)
        verbose_name = 'Department'
        verbose_name_plural = 'Departments'


class Location(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=500, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name

    def __repr__(self):
        return '<Location object ({})>'.format(self.id)

    class Meta:
        ordering = ('id',)
        verbose_name = 'Location'
        verbose_name_plural = 'Locations'


class Product(models.Model):
    DISCOUNT_RATE = 0.01
    name = models.CharField(max_length=500)
    description = models.CharField(max_length=300, blank=True, null=True)
    sku = models.CharField(max_length=100, unique=True)
    cost = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    price = models.DecimalField(
        max_digits=12, decimal_places=2, default=999.99)
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        default='1',
        related_name='department'
    )
    location = models.ForeignKey(
        Location,
        on_delete=models.CASCADE,
        default='1',
        related_name='location'
    )
    onhand_quantity = models.IntegerField(default=0)
    sale_start = models.DateTimeField(blank=True, null=True, default=None)
    sale_end = models.DateTimeField(blank=True, null=True, default=None)
    notes = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=True)
    photo = models.ImageField(
        blank=True,
        null=True,
        default=None,
        upload_to='static/images/store/products'
    )
    url = models.CharField(max_length=200, blank=True, null=True)
    product_created_by = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        default=None,
        related_name='product_created_by',
        blank=True,
        null=True
    )
    product_updated_by = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        default=None,
        related_name='product_updated_by',
        blank=True,

        null=True)
    ms_url = models.CharField(max_length=300, blank=True, null=True)

    def is_on_sale(self):
        now = timezone.now()
        if self.sale_start:
            if self.sale_end:
                return self.sale_start <= now <= self.sale_end
            return self.sale_start <= now
        return False

    def get_rounded_price(self):
        return round(self.price, 2)

    def current_price(self):
        if self.is_on_sale():
            discounted_price = self.price * (1 - self.DISCOUNT_RATE)
            return round(discounted_price, 2)
        return self.get_rounded_price()

    def get_margin(self):
        if self.cost:
            margin = self.price - self.cost
            return round(margin, 2)
        return 0

    def get_markup(self):
        if self.cost:
            markup = (self.price / self.cost) * 100
            return round(markup, 2)
        return 0

    def __repr__(self):
        return '<Product object ({})>'.format(self.name)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('id',)
        verbose_name = 'Product'
        verbose_name_plural = 'Products'


class ShoppingCart(models.Model):
    customer = models.OneToOneField(Profile, on_delete=models.CASCADE,
                                    related_name='cart_customer')

    def __str__(self):
        return f"{self.customer.username}'s Shopping Cart"

    def get_sales_tax(self):
        tax_rate = 0.09  # 9% sales tax rate
        taxable_items = ShoppingCartItem.objects.filter(
            cart=self, product__department__taxable=True)
        total_taxable = sum(
            item.price * item.quantity for item in taxable_items)
        return total_taxable * Decimal(tax_rate)


class ShoppingCartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(ShoppingCart, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.product.name} x {self.quantity}"


class Order(models.Model):
    customer = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name='order_customer')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username}'s Order"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.product.name} x {self.quantity}"
