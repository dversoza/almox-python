# Generated by Django 4.0.3 on 2022-06-04 18:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('stands', '0001_initial'),
        ('persons', '0002_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='person',
            options={'ordering': ['name'], 'verbose_name': 'Pessoa', 'verbose_name_plural': 'Pessoas'},
        ),
        migrations.AlterField(
            model_name='person',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Data de Criação'),
        ),
        migrations.AlterField(
            model_name='person',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_%(class)ss', to=settings.AUTH_USER_MODEL, verbose_name='Criado por'),
        ),
        migrations.AlterField(
            model_name='person',
            name='document',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='CPF/CNPJ'),
        ),
        migrations.AlterField(
            model_name='person',
            name='is_business',
            field=models.BooleanField(default=False, help_text='Marque se a pessoa é uma empresa.', verbose_name='Pessoa Jurídica'),
        ),
        migrations.AlterField(
            model_name='person',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='person',
            name='phone',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Telefone'),
        ),
        migrations.AlterField(
            model_name='person',
            name='stand',
            field=models.ForeignKey(blank=True, help_text='Selecione a barraca em que a pessoa trabalha.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='staff', to='stands.stand', verbose_name='Barraca'),
        ),
        migrations.AlterField(
            model_name='person',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Data de Atualização'),
        ),
        migrations.AlterField(
            model_name='person',
            name='updated_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='updated_%(class)ss', to=settings.AUTH_USER_MODEL, verbose_name='Atualizado por'),
        ),
        migrations.AlterField(
            model_name='person',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Usuário'),
        ),
    ]