from rest_framework import viewsets
from .serializers import TeapotSerializer
from .models import Teapot_Message

class TeapotViewset(viewsets.ModelViewSet):
  queryset= Teapot_Message.objects.all()
  serializer_class= TeapotSerializer
