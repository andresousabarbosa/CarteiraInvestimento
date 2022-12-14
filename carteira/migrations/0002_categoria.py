# Generated by Django 4.1.2 on 2022-10-08 04:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('carteira', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_categoria', models.CharField(max_length=256)),
                ('percentual_alocacao', models.FloatField()),
                ('carteira', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carteira.carteira')),
            ],
        ),
    ]
