# Generated by Django 4.0.4 on 2022-05-26 19:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tarefa', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tarefa',
            options={'ordering': ('modificado',), 'verbose_name': 'Tarefa', 'verbose_name_plural': 'Tarefas'},
        ),
    ]
