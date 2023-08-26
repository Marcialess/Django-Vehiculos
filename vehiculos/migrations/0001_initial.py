# Generated by Django 4.2.3 on 2023-07-14 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(choices=[('1', 'Ford'), ('2', 'Toyota'), ('3', 'Fiat'), ('4', 'Chevrolet')], default='ford', max_length=20)),
                ('modelo', models.CharField(max_length=100)),
                ('serial_carroceria', models.CharField(max_length=50)),
                ('serial_motor', models.CharField(max_length=50)),
                ('categoria', models.CharField(choices=[('1', 'Particular'), ('2', 'Transporte'), ('3', 'Carga')], default='Particular', max_length=20)),
                ('precio', models.FloatField()),
                ('fecha_de_creacion', models.DateField()),
                ('fecha_de_modificacion', models.DateField()),
            ],
        ),
    ]
