from rest_framework import filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import *

from produto.api.serializers import ProdutoSerializer
from produto.models import Produto


class ProdutoViewSet(ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['nome', 'marca', 'codigo_de_barras']
    ordering_fields = ['nome', ]
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated, ]

    # def get_queryset(self):
    #     return self.queryset.get(usuario=self.request.user)
