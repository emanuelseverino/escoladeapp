from django.shortcuts import render
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'core/index.html'


class ObrigadoView(TemplateView):
    template_name = 'core/obrigado.html'

