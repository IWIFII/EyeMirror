from django.shortcuts import render
from django.http import HttpResponse
from . import models
from . import serializers
from rest_framework import viewsets
from rest_framework import permissions


# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


class TodolistViewSet(viewsets.ModelViewSet):
    queryset = models.Todolist.objects.all()
    serializer_class = serializers.TodolistSerializer
    permission_classes = [permissions.IsAuthenticated]


class VisionViewSet(viewsets.ModelViewSet):
    queryset = models.Vision.objects.all()
    serializer_class = serializers.VisionSerializer
    permission_classes = [permissions.IsAuthenticated]
