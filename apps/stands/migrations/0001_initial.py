# Generated by Django 4.0.3 on 2022-09-08 02:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('persons', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Stand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Data de Criação')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Data de Atualização')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Nome')),
                ('active', models.BooleanField(default=True, verbose_name='Ativa')),
                ('contact', models.CharField(help_text='Telefone ou celular do responsável pela barraca', max_length=100, null=True, verbose_name='Contato')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_%(class)ss', to=settings.AUTH_USER_MODEL, verbose_name='Criado por')),
                ('manager', models.ForeignKey(help_text='Responsável pela barraca', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='stand_manager', to='persons.person', verbose_name='Responsável')),
                ('updated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='updated_%(class)ss', to=settings.AUTH_USER_MODEL, verbose_name='Atualizado por')),
            ],
            options={
                'verbose_name': 'Barraca',
                'verbose_name_plural': 'Barracas',
                'ordering': ['name'],
            },
        ),
    ]
