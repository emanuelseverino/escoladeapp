from rest_framework import filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import *
from tarefa.api.serializers import TarefaSerializer
from tarefa.models import Tarefa


class TarefaViewSet(ModelViewSet):
    queryset = Tarefa.objects.all()
    serializer_class = TarefaSerializer
    filter_backends = [filters.SearchFilter]
    ordering_fields = ['-modificado', ]
    # permission_classes = [IsAuthenticatedOrReadOnly, ]

    def get_queryset(self):
        return self.queryset.filter()

