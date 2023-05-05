from rest_framework import viewsets
from .models import (
    Department,
    Location,
    DeviceDefect,
    Device,
    WorkOrderCart,
    WorkOrderCartItem,
    Order,
    OrderItem)
from .serializers import (
    DepartmentSerializer,
    LocationSerializer,
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
