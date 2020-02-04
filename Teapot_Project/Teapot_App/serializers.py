from rest_framework import serializers
from .models import Teapot_Message

class TeapotSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
     model = Teapot_Message
     fields ='__all__'