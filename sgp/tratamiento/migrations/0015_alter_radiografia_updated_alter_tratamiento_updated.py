# Generated by Django 5.0.1 on 2024-01-26 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tratamiento', '0014_alter_tratamiento_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='radiografia',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='tratamiento',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
