from rest_framework.serializers import ModelSerializer

from postagem.models import Postagem
from usuario.api.serializers import UsuarioPostagemSerializer


class PostagemSerializer(ModelSerializer):
    autor = UsuarioPostagemSerializer()

    class Meta:
        model = Postagem
        fields = ['id', 'foto', 'titulo', 'descricao', 'autor', 'criado', ]
