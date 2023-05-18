"""signo URL Configuration

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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from objects.views import select_manager
from users.views import AppLoginView, AppRegistration

urlpatterns = [
    path("admin/", admin.site.urls),
    path('dash/', include('core.urls')),
    path('login/', AppLoginView.as_view(), name='login'),
    path('registration/', AppRegistration.as_view(), name='registration'),
    path('', include('index.urls')),
    path('tasks/', include('tasks.urls')),
    path('select_manager/<reservation_id>', select_manager, name='select_manager'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = settings.ADMIN_SITE_HEADER