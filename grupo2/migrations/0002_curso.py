# Generated by Django 4.1.3 on 2022-11-03 13:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('grupo2', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('descripcion', models.TextField(null=True, verbose_name='Descripcion')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grupo2.categoria')),
                ('socios', models.ManyToManyField(to='grupo2.socio')),
            ],
        ),
    ]