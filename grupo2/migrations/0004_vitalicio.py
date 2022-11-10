# Generated by Django 4.1.3 on 2022-11-08 13:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('grupo2', '0003_inscripcion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vitalicio',
            fields=[
                ('socio_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='grupo2.socio')),
                ('fecha', models.DateField(verbose_name='00/00/000')),
            ],
            bases=('grupo2.socio',),
        ),
    ]
