from django.shortcuts import render
from rest_framework import viewsets

from .serializers import foodSerializer
from .models import food


class foodViewSet(viewsets.ModelViewSet):
    queryset = food.objects.all().order_by('name')
    serializer_class = foodSerializer

# Create your views here.
