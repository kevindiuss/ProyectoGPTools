# Generated by Django 3.2 on 2021-05-04 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tratamiento', '0004_alter_tratamiento_paciente'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tratamiento',
            name='imagenes',
            field=models.ImageField(blank=True, null=True, upload_to='tratamientos'),
        ),
        migrations.DeleteModel(
            name='Radiografia',
        ),
    ]