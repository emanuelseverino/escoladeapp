from django.contrib.auth import get_user_model
from drf_extra_fields.fields import Base64ImageField
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

Usuario = get_user_model()


class UsuarioSerializer(ModelSerializer):
    foto = Base64ImageField(required=False)

    class Meta:
        model = Usuario
        fields = ['foto', 'nome', 'sobrenome', 'celular', 'cidade', 'latitude', 'longitude', ]


class CriarUsuarioSerializer(ModelSerializer):
    nome = serializers.CharField(required=True)
    sobrenome = serializers.CharField(required=True)

    class Meta:
        model = Usuario
        fields = ['nome', 'sobrenome', 'celular', 'email', 'password', ]
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        usuario = Usuario(username=validated_data['email'], **validated_data)
        usuario.set_password(validated_data['password'])
        usuario.save()
        return usuario


class UsuarioPostagemSerializer(ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'foto', 'nome', 'sobrenome', ]
