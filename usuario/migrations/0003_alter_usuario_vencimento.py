# Generated by Django 4.0.4 on 2022-05-20 13:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0002_usuario_vencimento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='vencimento',
            field=models.DateTimeField(default=datetime.date(2022, 5, 20)),
        ),
    ]