from django.contrib import admin
from django.urls import path, include

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from core.api.views import CreateUserView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user/register/', CreateUserView.as_view(), name="register "),
    # rest_framework_simplejwt views
    path('api/token/', TokenObtainPairView.as_view(), name='get_token'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # rest_framework views
    path('api-auth/', include("rest_framework.urls")),
    # api app
    path('api/', include("core.api.urls")),
]
