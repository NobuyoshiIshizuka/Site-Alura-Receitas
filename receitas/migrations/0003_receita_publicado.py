# Generated by Django 3.1.5 on 2021-01-17 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receitas', '0002_receita_pessoa'),
    ]

    operations = [
        migrations.AddField(
            model_name='receita',
            name='publicado',
            field=models.BooleanField(default=False),
        ),
    ]