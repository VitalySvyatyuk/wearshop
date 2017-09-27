from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from wear.views import ProductViewSet, CategoryViewSet, products

router = routers.DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'categories', CategoryViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/v/1/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^products/', products)
]
