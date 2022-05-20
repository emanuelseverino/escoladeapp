from rest_framework import permissions
from django.utils import timezone


class AssinaturaPermission(permissions.BasePermission):
    message = 'Token expirado, você precisa renovar sua assinatura entre em contato +5522997990159.'

    def has_permission(self, request, view):
        vencimento = request.user.vencimento
        hoje = timezone.now()
        if hoje == None or hoje >= vencimento:
            return False
        return True
