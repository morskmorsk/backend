from rest_framework.routers import DefaultRouter
from .api_views import (
    DepartmentViewSet,
    LocationViewSet,
    ProductViewSet,
    ShoppingCartViewSet,
    ShoppingCartItemViewSet,
    OrderViewSet,
    OrderItemViewSet,
    DeviceDefectViewSet,
    DeviceViewSet,
    WorkOrderCartViewSet,
    WorkOrderCartItemViewSet,

    )

router = DefaultRouter()
router.register(r'departments', DepartmentViewSet)
router.register(r'locations', LocationViewSet)
router.register(r'products', ProductViewSet)
router.register(r'shoppingcarts', ShoppingCartViewSet)
router.register(r'shoppingcartitems', ShoppingCartItemViewSet)
router.register(r'defects', DeviceDefectViewSet)
router.register(r'devices', DeviceViewSet)
router.register(r'workorders', WorkOrderCartViewSet)
router.register(r'workorderitems', WorkOrderCartItemViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'orderitems', OrderItemViewSet)
