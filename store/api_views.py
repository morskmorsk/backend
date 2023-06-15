from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
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
    permission_classes = [IsAuthenticated]


class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    permission_classes = [IsAuthenticated]


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]


class ShoppingCartViewSet(viewsets.ModelViewSet):
    queryset = ShoppingCart.objects.all()
    serializer_class = ShoppingCartSerializer
    permission_classes = [IsAuthenticated]


class ShoppingCartItemViewSet(viewsets.ModelViewSet):
    queryset = ShoppingCartItem.objects.all()
    serializer_class = ShoppingCartItemSerializer
    permission_classes = [IsAuthenticated]


class DeviceDefectViewSet(viewsets.ModelViewSet):
    queryset = DeviceDefect.objects.all()
    serializer_class = DeviceDefectSerializer
    permission_classes = [IsAuthenticated]


class DeviceViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    permission_classes = [IsAuthenticated]


class WorkOrderCartViewSet(viewsets.ModelViewSet):
    queryset = WorkOrderCart.objects.all()
    serializer_class = WorkOrderCartSerializer
    permission_classes = [IsAuthenticated]


class WorkOrderCartItemViewSet(viewsets.ModelViewSet):
    queryset = WorkOrderCartItem.objects.all()
    serializer_class = WorkOrderCartItemSerializer
    permission_classes = [IsAuthenticated]


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]


class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    permission_classes = [IsAuthenticated]
