from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from brands.views import main, brand_detail
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main),
    path('brand/<int:brand_id>/', brand_detail)
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
