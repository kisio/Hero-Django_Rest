from django.shortcuts import render
from rest_framework import viewsets
from .serializers import HeroSerializer
from .models import Hero

class HeroViewSet(viewsets.ModelViewSet):
    # Query db for heros
    queryset=Hero.objects.all().order_by('name')
    # convert to json
    serializer_class=HeroSerializer

