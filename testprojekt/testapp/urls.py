from django.urls import path, include
from rest_framework import routers
from .views import TodoView
from .views import GebaeudeerstellenView


router = routers.DefaultRouter()
router.register('todos', TodoView, 'todo')
router.register("gebaeudeerstellen", GebaeudeerstellenView, "gebaeudeerstellen")

urlpatterns = [
    path('', include(router.urls)),
]


