# Generated by Django 3.2 on 2021-05-03 23:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tratamiento', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Radiografias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagenes', models.ImageField(upload_to='radiografias/')),
                ('tratamiento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tratamiento.tratamiento')),
            ],
        ),
    ]