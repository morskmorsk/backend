from django.contrib import admin
from .models import (
    Department,
    Location,
    Product,
    ShoppingCart,
    ShoppingCartItem,
    DeviceDefect,
    Device,
    WorkOrderCart,
    WorkOrderCartItem,
    Order,
    OrderItem)

# Register your models here.

admin.site.register(Department)
admin.site.register(Location)
admin.site.register(Product)
admin.site.register(ShoppingCart)
admin.site.register(ShoppingCartItem)
admin.site.register(DeviceDefect)
admin.site.register(Device)
admin.site.register(WorkOrderCart)
admin.site.register(WorkOrderCartItem)
admin.site.register(Order)
admin.site.register(OrderItem)

