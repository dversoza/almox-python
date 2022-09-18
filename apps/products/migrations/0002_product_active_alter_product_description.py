# Generated by Django 4.1.1 on 2022-09-14 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="active",
            field=models.BooleanField(default=True, verbose_name="Ativo"),
        ),
        migrations.AlterField(
            model_name="product",
            name="description",
            field=models.TextField(
                blank=True,
                help_text="Descrição do produto",
                null=True,
                verbose_name="Descrição",
            ),
        ),
    ]