# Generated by Django 3.1.2 on 2020-10-05 11:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Campus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('suap_id', models.CharField(max_length=255, unique=True, verbose_name='ID no SUAP')),
                ('sigla', models.CharField(max_length=255, unique=True, verbose_name='Sigla')),
                ('descricao', models.CharField(max_length=255, verbose_name='Descrição')),
                ('url', models.URLField(max_length=255, verbose_name='URL')),
                ('thumbnail', models.ImageField(max_length=255, upload_to='', verbose_name='Sigla')),
                ('active', models.BooleanField(verbose_name='Ativo')),
            ],
            options={
                'verbose_name': 'Campus',
                'verbose_name_plural': 'Campi',
                'ordering': ['sigla'],
            },
        ),
        migrations.CreateModel(
            name='Solicitacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(verbose_name='Quando ocorreu')),
                ('requisicao', models.TextField(blank=True, null=True, verbose_name='Requisição')),
                ('requisicao_header', models.TextField(blank=True, null=True, verbose_name='Cabeçalho da requisição')),
                ('requisicao_invalida', models.TextField(blank=True, null=True, verbose_name='Requisição inválida')),
                ('resposta', models.TextField(blank=True, null=True, verbose_name='Resposta')),
                ('resposta_header', models.TextField(blank=True, null=True, verbose_name='Cabeçalho da resposta')),
                ('resposta_invalida', models.TextField(blank=True, null=True, verbose_name='Resposta inválida')),
                ('status', models.CharField(blank=True, choices=[('Sucesso', 'Sucesso'), ('Falha', 'Falha')], max_length=255, null=True, verbose_name='Kind')),
                ('campus', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='avaportal.campus', verbose_name='Campus')),
            ],
            options={
                'verbose_name': 'Solicitação',
                'verbose_name_plural': 'Solicitações',
                'ordering': ['id'],
            },
        ),
    ]
