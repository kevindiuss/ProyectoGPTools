# Generated by Django 5.0.4 on 2024-07-26 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacunas', '0005_remove_vacunaspacientes_dpt_acelular_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vacunaspacientes',
            old_name='DPT_ACELULAR_1R',
            new_name='DPT_ACELULAR_R1',
        ),
        migrations.RenameField(
            model_name='vacunaspacientes',
            old_name='DPT_ACELULAR_2R',
            new_name='DPT_ACELULAR_R2',
        ),
        migrations.RenameField(
            model_name='vacunaspacientes',
            old_name='DPT_ACELULAR_3R',
            new_name='DPT_ACELULAR_R3',
        ),
        migrations.RemoveField(
            model_name='vacunaspacientes',
            name='NEUMOCOCO_CONJUGADO',
        ),
        migrations.AddField(
            model_name='vacunaspacientes',
            name='NEUMOCOCO_CONJUGADO_1',
            field=models.CharField(default='no', max_length=50, verbose_name='NEUMOCON1'),
        ),
        migrations.AddField(
            model_name='vacunaspacientes',
            name='NEUMOCOCO_CONJUGADO_2',
            field=models.CharField(default='no', max_length=50, verbose_name='NEUMOCON2'),
        ),
        migrations.AddField(
            model_name='vacunaspacientes',
            name='NEUMOCOCO_CONJUGADO_3',
            field=models.CharField(default='no', max_length=50, verbose_name='NEUMOCON3'),
        ),
        migrations.AddField(
            model_name='vacunaspacientes',
            name='NEUMOCOCO_CONJUGADO_4',
            field=models.CharField(default='no', max_length=50, verbose_name='NEUMOCON4'),
        ),
        migrations.AddField(
            model_name='vacunaspacientes',
            name='NEUMOCOCO_CONJUGADO_5',
            field=models.CharField(default='no', max_length=50, verbose_name='NEUMOCON5'),
        ),
        migrations.AddField(
            model_name='vacunaspacientes',
            name='NEUMOCOCO_CONJUGADO_R1',
            field=models.CharField(default='no', max_length=50, verbose_name='NEUMOCONR1'),
        ),
        migrations.AddField(
            model_name='vacunaspacientes',
            name='NEUMOCOCO_CONJUGADO_R2',
            field=models.CharField(default='no', max_length=50, verbose_name='NEUMOCONR2'),
        ),
        migrations.AddField(
            model_name='vacunaspacientes',
            name='NEUMOCOCO_CONJUGADO_R3',
            field=models.CharField(default='no', max_length=50, verbose_name='NEUMOCONR3'),
        ),
        migrations.AddField(
            model_name='vacunaspacientes',
            name='NEUMOCOCO_CONJUGADO_U',
            field=models.CharField(default='no', max_length=50, verbose_name='NEUMOCONU'),
        ),
    ]
