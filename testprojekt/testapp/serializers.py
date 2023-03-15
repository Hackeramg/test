from rest_framework import serializers
from .models import Todo
from .models import Gebaeudeerstellen

class TodoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Todo
        fields = ("id", "Ersteller", "Lernfeld", "Beschreibung", "is_done", "created_at", "updated_at")
        

class GebaeudeerstellenSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Gebaeudeerstellen
        fields = ("id", "owner", "name", "street", "number", "postalcode", "city", "lon", "lat")
        
        