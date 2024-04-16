# Generated by Django 5.0.4 on 2024-04-12 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paciente', '0011_rename_emergencia_paciente_aseguradora_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='paciente',
            old_name='RH',
            new_name='rh',
        ),
        migrations.RenameField(
            model_name='paciente',
            old_name='tipoAfiliacion',
            new_name='tipoAfi',
        ),
        migrations.RemoveField(
            model_name='paciente',
            name='grupoSanguineo',
        ),
        migrations.AddField(
            model_name='paciente',
            name='sangre',
            field=models.CharField(default=0, max_length=15),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='paciente',
            name='fecha_nacimiento',
            field=models.DateField(verbose_name='fechaNacimiento'),
        ),
    ]