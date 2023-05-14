from rest_framework import viewsets
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
from .serializers import (
    DepartmentSerializer,
    LocationSerializer,
    ProductSerializer,
    ShoppingCartSerializer,
    ShoppingCartItemSerializer,
    DeviceDefectSerializer,
    DeviceSerializer,
    WorkOrderCartSerializer,
    WorkOrderCartItemSerializer,
    OrderSerializer,
    OrderItemSerializer)


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ShoppingCartViewSet(viewsets.ModelViewSet):
    queryset = ShoppingCart.objects.all()
    serializer_class = ShoppingCartSerializer


class ShoppingCartItemViewSet(viewsets.ModelViewSet):
    queryset = ShoppingCartItem.objects.all()
    serializer_class = ShoppingCartItemSerializer


class DeviceDefectViewSet(viewsets.ModelViewSet):
    queryset = DeviceDefect.objects.all()
    serializer_class = DeviceDefectSerializer


class DeviceViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer


class WorkOrderCartViewSet(viewsets.ModelViewSet):
    queryset = WorkOrderCart.objects.all()
    serializer_class = WorkOrderCartSerializer


class WorkOrderCartItemViewSet(viewsets.ModelViewSet):
    queryset = WorkOrderCartItem.objects.all()
    serializer_class = WorkOrderCartItemSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
