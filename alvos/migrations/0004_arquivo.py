# Generated by Django 3.2.3 on 2021-07-26 12:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('alvos', '0003_email_notas'),
    ]

    operations = [
        migrations.CreateModel(
            name='Arquivo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Arquivo', models.ImageField(upload_to='')),
                ('Notas', models.TextField()),
                ('Pessoa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alvos.pessoa')),
            ],
        ),
    ]
