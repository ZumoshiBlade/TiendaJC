from django.core.exceptions import ValidationError
from rest_framework import fields, serializers
from .models import *
from django.db.models.query import QuerySet

class tipoSuscripcionSerializer(serializers.ModelSerializer):
    class Meta:
        model = suscripcion
        fields = '__all__'

class SuscripcionSerializer(serializers.ModelSerializer):
    descripcion = tipoSuscripcionSerializer(read_only=True)
    tipo_suscripcion =  serializers.PrimaryKeyRelatedField(queryset = suscripcion.objects.all(),source = "descripcion")
    class Meta:
        model = suscriptUser
        fields = '__all__'
    
    def validate_usuario(self, value):
        existe = suscriptUser.objects.filter(usuario__iexact=value).exists()
        
        if existe:
            raise ValidationError('¡Ya tienes suscripción!')
        
        return value
    
    def validate_email(self, value):
        existe = suscriptUser.objects.filter(email__iexact=value).exists()
        
        if existe:
            raise ValidationError('¡Ya tienes suscripción!')
        
        return value
    
