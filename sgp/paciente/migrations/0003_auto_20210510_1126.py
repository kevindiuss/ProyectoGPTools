# Generated by Django 3.2 on 2021-05-10 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paciente', '0002_alter_paciente_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='paciente',
            name='direccion',
            field=models.CharField(default=1, max_length=150, verbose_name='dirección'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='paciente',
            name='historia_clinica',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]