# Generated by Django 4.0.4 on 2022-05-22 12:33

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0008_alter_usuario_vencimento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='vencimento',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 22, 12, 33, 36, 99400, tzinfo=utc)),
            preserve_default=False,
        ),
    ]