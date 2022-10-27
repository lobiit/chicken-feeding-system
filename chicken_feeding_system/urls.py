"""chicken_feeding_system URL Configuration

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
from django.urls import path
from feeder import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.feeder_list_create_view, name="feeder-list"),
    path("<int:pk>/", views.feeder_detail_view, name="feeder-detail"),
    path("refill/<int:pk>/", views.feeder_refill_view, name="feeder-refill"),
    path("delete/<int:pk>/", views.feeder_delete_view),

]
