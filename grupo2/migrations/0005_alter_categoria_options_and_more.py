# Generated by Django 4.1.4 on 2022-12-07 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grupo2', '0004_alter_comprobante_comprobante_alter_cuota_cuota'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categoria',
            options={'verbose_name_plural': 'Categorias'},
        ),
        migrations.AlterModelOptions(
            name='ciudadresidencia',
            options={'verbose_name_plural': 'Ciudades'},
        ),
        migrations.AlterModelOptions(
            name='comprobante',
            options={'verbose_name_plural': 'Comprobantes'},
        ),
        migrations.AlterModelOptions(
            name='cuota',
            options={'verbose_name_plural': 'Cuotas'},
        ),
        migrations.AlterModelOptions(
            name='curso',
            options={'verbose_name_plural': 'Cursos'},
        ),
        migrations.AlterModelOptions(
            name='socio',
            options={'verbose_name_plural': 'Socios'},
        ),
        migrations.RemoveField(
            model_name='socio',
            name='expediente',
        ),
        migrations.AlterField(
            model_name='curso',
            name='imagen',
            field=models.FileField(null=True, upload_to='../media/', verbose_name='Imagen a mostrar'),
        ),
    ]
