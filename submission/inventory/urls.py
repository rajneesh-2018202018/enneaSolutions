from webbrowser import get
from django.urls import include, path

from rest_framework import routers

from inventory.views import InventoryViewSet, UploadFileView, Unexpired

router = routers.DefaultRouter()
router.register(r'inventory', InventoryViewSet)

urlpatterns = [
   path('', include(router.urls)),
   path('upload/', UploadFileView.as_view(), name='upload-file'),
   path('unexpired/', Unexpired.as_view({'get': 'list'}))
]