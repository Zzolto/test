from unittest.util import _MAX_LENGTH
from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import *
import io



class TypeNewsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = ('title', 'color')

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('title', 'shortDescription','fullDescription', 'newsType')

    # def delete(self, validated_data, **kwargs):
    #     deleteObj = News.objects.delete(**validated_data)
    #     deleteObj.delete()
        
