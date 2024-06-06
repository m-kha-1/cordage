from .models import *
from rest_framework import serializers

class ProdSerializer(serializers.ModelSerializer):
    class Meta:
        model=PRODUCTION
        fields='__all__'
        
# class TaskSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=Task
#         fields='__all__'
#         read_only_fields = ['id']
        
class TaskSerializer2(serializers.ModelSerializer):
    class Meta:
        model=Task2
        fields = '__all__'
        read_only_fields = ['id']
        
class TaskSerializer2_noId(serializers.ModelSerializer):
    producer_name = serializers.CharField(source='producerID.name', read_only=True)
    production_name = serializers.CharField(source='PRODUCTIONId.name', read_only=True)
    cgSupervisor2_name=serializers.CharField(source='supervisor2ID.name', read_only=True)
    cgArtist_name=serializers.CharField(source='cgArtist3Id.name', read_only=True)
    
    class Meta:
        model=Task2
        fields='__all__'
        # fields = ['id', 'name', 'type', 'dateCreated', 'dateDue', 'completed','production_name','cgArtist_name','producer_name']
        read_only_fields = ['id']
        
    # def get_production_name(self, obj):
    #     # Accéder à l'objet lié et à son attribut de chaîne
    #     return obj.PRODUCTIONId.name if obj.PRODUCTIONId else None

    # def get_cgArtist_name(self, obj):
    #     # Accéder à l'objet lié et à son attribut de chaîne
    #     return obj.cgArtistId.name if obj.cgArtistId else None
        
   
        
        
        
        
        
class ProducerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Producer
        fields='__all__'
        
class Producer2Serializer(serializers.ModelSerializer):
    class Meta:
        model=Producer2
        fields='__all__'
        
class CgArtist2Serializer(serializers.ModelSerializer):
    class Meta:
        model=CgArtist3
        fields='__all__'
        
class Supervisor2Serializer(serializers.ModelSerializer):
    class Meta:
        model=Supervisor2
        fields='__all__'
        
    
        
        
