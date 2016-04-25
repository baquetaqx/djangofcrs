# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-25 19:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evento', '0004_inscricao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='cidade',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='cpf',
            field=models.CharField(blank=True, max_length=200, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='estado',
            field=models.CharField(blank=True, choices=[('', 'UF'), ('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amap\xe1'), ('BA', 'Bahia'), ('CE', 'Cear\xe1'), ('DF', 'Distrito Federal'), ('ES', 'Esp\xedrito Santo'), ('GO', 'Goi\xe1s'), ('MA', 'Maranh\xe3o'), ('MG', 'Minas Gerais'), ('MS', 'Mato Grosso do Sul'), ('MT', 'Mato Grosso'), ('PA', 'Par\xe1'), ('PB', 'Para\xedba'), ('PE', 'Pernambuco'), ('PI', 'Piau\xed'), ('PR', 'Paran\xe1'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RO', 'Rond\xf4nia'), ('RR', 'Roraima'), ('RS', 'Rio Grande do Sul'), ('SC', 'Santa Catarina'), ('SE', 'Sergipe'), ('SP', 'S\xe3o Paulo'), ('TO', 'Tocantins')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='genero',
            field=models.CharField(blank=True, choices=[('', 'G\xeanero'), ('MASCULINO', 'Masculino'), ('FEMININO', 'Feminino')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='idade',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='telefone',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]