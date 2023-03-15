from django.shortcuts import render
from rest_framework import viewsets
from .models import Todo
from .serializers import TodoSerializer
from .models import Gebaeudeerstellen
from .serializers import GebaeudeerstellenSerializer
# Create your views here.


class TodoView(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    
    def get_queryset(self):
        queryset = Todo.objects.all()
        return queryset

class GebaeudeerstellenView(viewsets.ModelViewSet):
    queryset = Gebaeudeerstellen.objects.all()
    serializer_class = GebaeudeerstellenSerializer
    
    def get_queryset(self):
        querset = Gebaeudeerstellen.objects.all()
        return querset
        