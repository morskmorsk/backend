"""api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from accounts.routers import router as accounts_router
from store.routers import router as store_router
from accounts.views import MyTokenObtainPairView, MyTokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include(accounts_router.urls),
         name='users_api'),
    path('', include(store_router.urls),
         name='store_api'),
    path('api/token/', MyTokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('api/token/refresh/', MyTokenRefreshView.as_view(),
         name='token_refresh'),

    # path('api/token/', ObtainToken.as_view()),
    # path('api-auth/', include('rest_framework.urls'),
    #      name='api-auth'),
    # path('users/', include('accounts.urls'),
    #      name='users_api'),
]
