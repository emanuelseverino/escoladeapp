from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken.views import obtain_auth_token

from postagem.api.viewsets import PostagemViewSet
from produto.api.viewsets import ProdutoViewSet, ProdutoTodosViewSet
from tarefa.api.viewsets import TarefaViewSet
from usuario.api.viewsets import CriarUsuarioViewSet, UsuarioViewSet

router = routers.DefaultRouter()
router.register(r'usuario', UsuarioViewSet)
router.register(r'cadastro', CriarUsuarioViewSet)
router.register(r'produto', ProdutoViewSet)
router.register(r'postagem', PostagemViewSet)
router.register(r'tarefa', TarefaViewSet)
router.register(r'todos/produtos', ProdutoTodosViewSet)

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', include('core.urls')),
                  path('conta/', include('usuario.urls')),
                  path('api/', include(router.urls)),
                  path('login/', obtain_auth_token),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
