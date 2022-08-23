# Generated by Django 4.0.3 on 2022-08-23 01:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('stands', '0001_initial'),
        ('persons', '0001_initial'),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TransactionType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Data de Criação')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Data de Atualização')),
                ('operation', models.CharField(choices=[('E', 'Entrada'), ('S', 'Saida')], help_text='Entrada: produtos entrando no almoxarifado<br>Saída: produtos saindo do almoxarifado', max_length=1, verbose_name='Operação')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Nome')),
                ('description', models.TextField(blank=True, help_text='Descrição do tipo de movimentação', max_length=500, null=True, verbose_name='Descrição')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_%(class)ss', to=settings.AUTH_USER_MODEL, verbose_name='Criado por')),
                ('updated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='updated_%(class)ss', to=settings.AUTH_USER_MODEL, verbose_name='Atualizado por')),
            ],
            options={
                'verbose_name': 'Tipo de movimentação',
                'verbose_name_plural': 'Tipos de movimentação',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Data de Criação')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Data de Atualização')),
                ('datetime', models.DateTimeField(help_text='Data e hora da movimentação', verbose_name='Data e Hora')),
                ('operation', models.CharField(choices=[('E', 'Entrada'), ('S', 'Saida')], default='S', help_text='Entrada: produtos entrando no almoxarifado<br>Saída: produtos saindo do almoxarifado', max_length=1, verbose_name='Operação')),
                ('quantity', models.FloatField(verbose_name='Quantidade')),
                ('price', models.IntegerField(help_text='Valor global da movimentação <b>em centavos</b>; 0 (zero) para saídas internas e devoluções', verbose_name='Preço')),
                ('details', models.TextField(blank=True, null=True, verbose_name='Observações')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_%(class)ss', to=settings.AUTH_USER_MODEL, verbose_name='Criado por')),
                ('person', models.ForeignKey(help_text='Pessoa responsável pela movimentação', on_delete=django.db.models.deletion.CASCADE, to='persons.person', verbose_name='Pessoa')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product', verbose_name='Produto')),
                ('stand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stands.stand', verbose_name='Barraca')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='transactions.transactiontype', verbose_name='Tipo')),
                ('updated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='updated_%(class)ss', to=settings.AUTH_USER_MODEL, verbose_name='Atualizado por')),
            ],
            options={
                'verbose_name': 'Movimentação',
                'verbose_name_plural': 'Movimentações',
                'ordering': ['-created_at', '-updated_at'],
            },
        ),
    ]
