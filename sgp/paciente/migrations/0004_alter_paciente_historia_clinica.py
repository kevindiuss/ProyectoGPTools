# Generated by Django 3.2 on 2021-05-10 15:39

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('paciente', '0003_auto_20210510_1126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='historia_clinica',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
