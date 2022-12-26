"""zhiyi_api URL Configuration

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
from django.urls import path, include, re_path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)
from apiv1.auth.views import ZhiyiTokenObtainPairView
# 文档相关
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Zhiyi API",
      default_version='v1',
      description="这是一个接口文档",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="81784779@qq.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    # 管理站点
    path('admin/', admin.site.urls),
    # API文档
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    # path('apiv1/auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('apiv1/auth/token/', ZhiyiTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('apiv1/auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('apiv1/auth/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('apiv1/', include('apiv1.urls'))
]
