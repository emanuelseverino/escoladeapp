from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import UsuarioChangeForm, UsuarioCreationForm
from .models import Usuario


@admin.register(Usuario)
class UsuarioAdmin(UserAdmin):
    add_form = UsuarioCreationForm
    form = UsuarioChangeForm
    model = Usuario
    list_display = ('email', 'nome', 'sobrenome', 'celular', 'is_staff', 'vencimento', )
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Informações Pessoais', {'fields': ('pago', 'nome', 'sobrenome', 'celular', 'cidade', 'vencimento')}),
        ('Permissões', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Datas Importantes', {'fields': ('last_login', 'date_joined')}),
    )
