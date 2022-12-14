# Generated by Django 4.1.4 on 2022-12-12 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grupo2', '0008_auto_20221211_1209'),
    ]

    operations = [
        migrations.AddField(
            model_name='curso',
            name='dia',
            field=models.CharField(choices=[('1', 'Lunes'), ('2', 'Martes'), ('3', 'Miercoles'), ('4', 'Jueves'), ('5', 'Viernes'), ('6', 'Sabado'), ('7', 'Domingo'), ('8', 'Semanal'), ('9', 'Mensual'), ('0', 'Unica vez')], default='1', max_length=1, verbose_name='Dias'),
        ),
        migrations.AddField(
            model_name='curso',
            name='turno',
            field=models.CharField(choices=[('1', '8 a 10Hs'), ('2', '10 a 12Hs'), ('3', '12 a 14Hs'), ('4', '14 a 16Hs'), ('5', '16 a 18Hs'), ('6', '18 a 20Hs'), ('7', '20 a 22Hs')], default='1', max_length=1, verbose_name='Turno'),
        ),
    ]
