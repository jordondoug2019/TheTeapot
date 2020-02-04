from django.shortcuts import render
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.

from django.shortcuts import render


class Index(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'index.html'