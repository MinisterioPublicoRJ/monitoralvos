# Generated by Django 3.2.3 on 2021-05-30 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alvos', '0002_anotacao_entradaagenda_telefone'),
    ]

    operations = [
        migrations.AddField(
            model_name='email',
            name='Notas',
            field=models.TextField(blank=True, null=True),
        ),
    ]
