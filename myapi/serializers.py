#serializers convert database objects to JSON 
# import hero model
from .models import Hero
# import the rest framework
from rest_framework import serializers
# create new class that links the serializer with hero
class HeroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Hero
        fields=['id','name','alias']