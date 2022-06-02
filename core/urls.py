from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken.views import obtain_auth_token

from core.views import IndexView, ObrigadoView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('obrigado/', ObrigadoView.as_view(), name='obrigado'),
]
