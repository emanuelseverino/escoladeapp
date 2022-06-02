from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView

from usuario.forms import UserAdminCreationForm

from usuario.models import Usuario


class RegisterView(CreateView):
    model = Usuario
    template_name = 'usuario/register.html'
    form_class = UserAdminCreationForm
    success_url = reverse_lazy('obrigado')

    def form_valid(self, form):
        return super().form_valid(form)
