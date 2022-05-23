from django.urls import path
from rest_framework import routers
from . import views

# router = routers.DefaultRouter()
# router.register(r'todolist',views.TodoViewSet)
urlpatterns = [
    path('', views.index, name='index'),
    # path('', views.TodolistList.as_view()),
    # path('', include(router.urls)),
]
