"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from general.views.top_view import TopView
from general.views.shop_detail_view import ShopDetailView
from general.views.shop_list_view import ShopListView
from general.views.review_view import submit_review

urlpatterns = [
    path('admin/', admin.site.urls),
    path('general/', TopView.as_view(), name="top"),
    path('general/shop_detail/<int:pk>/', ShopDetailView.as_view(), name="shop_detail"),
    path('general/shop_list/', ShopListView.as_view(), name="shop_list"),
    path('general/submit_review/', submit_review, name="submit_review"),
]

# MEDIA_URL に対する URL パターンを追加します
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
