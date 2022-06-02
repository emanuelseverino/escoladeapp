from rest_framework import filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import *

from postagem.api.serializers import PostagemSerializer
from postagem.models import Postagem


class PostagemViewSet(ModelViewSet):
    queryset = Postagem.objects.all()
    serializer_class = PostagemSerializer
    filter_backends = [filters.SearchFilter]
    ordering_fields = ['-criado', ]
    permission_classes = [IsAuthenticatedOrReadOnly, ]

    def get_queryset(self):
        return self.queryset.filter()

