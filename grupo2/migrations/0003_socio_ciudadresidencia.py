# Generated by Django 4.1.3 on 2022-11-28 02:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('grupo2', '0002_alter_ciudadresidencia_codigopostal'),
    ]

    operations = [
        migrations.AddField(
            model_name='socio',
            name='ciudadResidencia',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='grupo2.ciudadresidencia', verbose_name='Ciudad'),
        ),
    ]
