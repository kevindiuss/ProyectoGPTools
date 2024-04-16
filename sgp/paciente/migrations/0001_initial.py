# Generated by Django 3.2 on 2021-05-03 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='nombre')),
                ('apellido', models.CharField(max_length=50, verbose_name='apellido')),
                ('cedula', models.CharField(max_length=15, verbose_name='cédula')),
                ('telefono', models.CharField(max_length=20, verbose_name='teléfono')),
                ('fecha_nacimiento', models.DateField(verbose_name='fecha de nacimiento')),
                ('email', models.EmailField(max_length=254, verbose_name='email')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['created'],
            },
        ),
    ]
