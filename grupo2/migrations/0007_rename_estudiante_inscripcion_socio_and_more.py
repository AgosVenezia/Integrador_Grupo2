# Generated by Django 4.1.4 on 2022-12-09 03:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grupo2', '0006_alter_curso_imagen'),
    ]

    operations = [
        migrations.RenameField(
            model_name='inscripcion',
            old_name='estudiante',
            new_name='socio',
        ),
        migrations.RemoveField(
            model_name='curso',
            name='socios',
        ),
        migrations.AlterField(
            model_name='curso',
            name='imagen',
            field=models.FileField(null=True, upload_to='imagen_curso/', verbose_name='Imagen a mostrar'),
        ),
    ]