# Generated by Django 3.1.4 on 2021-01-09 20:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_empresa', models.CharField(max_length=100)),
                ('logo_empresa', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_produto', models.CharField(max_length=100)),
                ('descricao_produto', models.CharField(max_length=200)),
                ('valor_produto', models.FloatField(default=0)),
                ('quantidade_produto', models.IntegerField(default=0)),
                ('empresa_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loja.empresa')),
            ],
        ),
    ]
