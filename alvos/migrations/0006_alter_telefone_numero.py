# Generated by Django 3.2.3 on 2021-07-28 16:10

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alvos', '0005_alter_arquivo_arquivo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='telefone',
            name='numero',
            field=models.CharField(max_length=18, validators=[django.core.validators.RegexValidator('\\d{10,}', code='telinfalido', message='Informe telefone no formato 552199998888, com pelo menos 9 números')]),
        ),
    ]
