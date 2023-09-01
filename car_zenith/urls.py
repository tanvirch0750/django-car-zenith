from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('account/', include('account.urls')),
    # path('brand/', include('brand.urls')),
    path('car/', include('car.urls')),
    # path('orders/', include('orders.urls')),
    # path('cart/', include('cart.urls')),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
