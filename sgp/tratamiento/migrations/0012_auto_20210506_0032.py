# Generated by Django 3.2 on 2021-05-06 03:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tratamiento', '0011_auto_20210505_2329'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tratamiento',
            name='radiografias',
        ),
        migrations.AddField(
            model_name='radiografia',
            name='tratamiento',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='tratamiento.tratamiento'),
            preserve_default=False,
        ),
    ]