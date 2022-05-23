from rest_framework import serializers
from . import models
from .models import Todolist
from .models import Vision


class TodolistSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'content')
        model = Todolist


class VisionSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'leftEye', 'rightEye', 'date')
        model = Vision
