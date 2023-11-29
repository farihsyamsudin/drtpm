# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'data_penangkapan', DataPenangkapanViewSet)
router.register(r'nelayan', NelayanViewset)
router.register(r'kapal', KapalViewset)

urlpatterns = [
    path('', include(router.urls)),
]