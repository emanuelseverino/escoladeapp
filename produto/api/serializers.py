from django.contrib.auth import get_user_model
from drf_extra_fields.fields import Base64ImageField
from rest_framework.serializers import ModelSerializer

from produto.models import Produto
from usuario.api.serializers import UsuarioSerializer

Usuario = get_user_model()


class ProdutoSerializer(ModelSerializer):
    usuario = UsuarioSerializer()
    foto = Base64ImageField(required=False)

    class Meta:
        model = Produto
        fields = '__all__'
        # fields = ['foto', 'nome', 'sobrenome', 'celular', 'cidade', 'latitude', 'longitude', ]


class ProdutoTodosSerializer(ModelSerializer):

    class Meta:
        model = Produto
        fields = ['foto', 'nome', 'marca', 'descricao', 'preco', 'codigo_de_barras',]
