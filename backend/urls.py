from django.contrib import admin
from django.urls import path

from core.api.views import CreateUserView

urlpatterns = [
    path('admin/', admin.site.urls),

]
