from rest_framework import routers 
from .api import TeapotViewset
from django.urls import include, path
from . import views

router = routers.DefaultRouter()

router.register('api/theteapot', TeapotViewset)

urlpatterns = [ path('', include(router.urls)),
]