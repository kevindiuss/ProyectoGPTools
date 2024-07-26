# Generated by Django 5.0.4 on 2024-07-26 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacunas', '0006_rename_dpt_acelular_1r_vacunaspacientes_dpt_acelular_r1_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vacunaspacientes',
            name='ANTIRRABICA',
        ),
        migrations.RemoveField(
            model_name='vacunaspacientes',
            name='COVID',
        ),
        migrations.RemoveField(
            model_name='vacunaspacientes',
            name='FIEBRE_AMARILLA',
        ),
        migrations.RemoveField(
            model_name='vacunaspacientes',
            name='FIEBRE_TIFOIDEA',
        ),
        migrations.RemoveField(
            model_name='vacunaspacientes',
            name='HA_HB',
        ),
        migrations.RemoveField(
            model_name='vacunaspacientes',
            name='HEPATITIS_A',
        ),
        migrations.RemoveField(
            model_name='vacunaspacientes',
            name='HEPATITIS_B',
        ),
        migrations.RemoveField(
            model_name='vacunaspacientes',
            name='HERPES_ZOSTER',
        ),
        migrations.RemoveField(
            model_name='vacunaspacientes',
            name='INFLUENZA',
        ),
        migrations.RemoveField(
            model_name='vacunaspacientes',
            name='MENINGOCOCO',
        ),
        migrations.RemoveField(
            model_name='vacunaspacientes',
            name='TETANO_ANTITETANICA',
        ),
        migrations.RemoveField(
            model_name='vacunaspacientes',
            name='TETANO_DIFTERICO',
        ),
        migrations.RemoveField(
            model_name='vacunaspacientes',
            name='TRIPLE_VIRAL',
        ),
        migrations.RemoveField(
            model_name='vacunaspacientes',
            name='VARICELA',
        ),
        migrations.RemoveField(
            model_name='vacunaspacientes',
            name='VPH',
        ),
        migrations.AddField(
            model_name='vacunaspacientes',
            name='ANTIRRABICA_1',
            field=models.CharField(default='no', max_length=50, verbose_name='ANTIRRABICA1'),
        ),
        migrations.AddField(
            model_name='vacunaspacientes',
            name='ANTIRRABICA_2',
            field=models.CharField(default='no', max_length=50, verbose_name='ANTIRRABICA2'),
        ),
        migrations.AddField(
            model_name='vacunaspacientes',
            name='ANTIRRABICA_3',
            field=models.CharField(default='no', max_length=50, verbose_name='ANTIRRABICA3'),
        ),
        migrations.AddField(
            model_name='vacunaspacientes',
            name='ANTIRRABICA_4',
            field=models.CharField(default='no', max_length=50, verbose_name='ANTIRRABICA4'),
        ),
        migrations.AddField(
            model_name='vacunaspacientes',
            name='ANTIRRABICA_5',
            field=models.CharField(default='no', max_length=50, verbose_name='ANTIRRABICA5'),
        ),
        migrations.AddField(
            model_name='vacunaspacientes',
            name='ANTIRRABICA_R1',
            field=models.CharField(default='no', max_length=50, verbose_name='ANTIRRABICAR1'),
        ),
        migrations.AddField(
            model_name='vacunaspacientes',
            name='ANTIRRABICA_R2',
            field=models.CharField(default='no', max_length=50, verbose_name='ANTIRRABICAR2'),
        ),
        migrations.AddField(
            model_name='vacunaspacientes',
            name='ANTIRRABICA_R3',
            field=models.CharField(default='no', max_length=50, verbose_name='ANTIRRABICAR3'),
        ),
        migrations.AddField(
            model_name='vacunaspacientes',
            name='ANTIRRABICA_U',
            field=models.CharField(default='no', max_length=50, verbose_name='ANTIRRABICAU'),
        ),
        migrations.AddField(
            model_name='vacunaspacientes',
            name='COVID_1',
            field=models.CharField(default='no', max_length=50, verbose_name='COVID1'),
        ),
        migrations.AddField(
            model_name='vacunaspacientes',
            name='COVID_2',
            field=models.CharField(default='no', max_length=50, verbose_name='COVID2'),
        ),
        migrations.AddField(
            model_name='vacunaspacientes',
            name='COVID_3',
            field=models.CharField(default='no', max_length=50, verbose_name='COVID3'),
        ),
        migrations.AddField(
            model_name='vacunaspacientes',
            name='COVID_4',
            field=models.CharField(default='no', max_length=50, verbose_name='COVID4'),
        ),
        migrations.AddField(
            model_name='vacunaspacientes',
            name='COVID_5',
            field=models.CharField(default='no', max_length=50, verbose_name='COVID5'),
        ),
        migrations.AddField(
            model_name='vacunaspacientes',
            name='COVID_R1',
            field=models.CharField(default='no', max_length=50, verbose_name='COVIDR1'),
        ),
        migrations.AddField(
            model_name='vacunaspacientes',
            name='COVID_R2',
            field=models.CharField(default='no', max_length=50, verbose_name='COVIDR2'),
        ),
        migrations.AddField(
            model_name='vacunaspacientes',
            name='COVID_R3',
            field=models.CharField(default='no', max_length=50, verbose_name='COVIDR3'),
        ),
        migrations.AddField(
            model_name='vacunaspacientes',
            name='COVID_U',
            field=models.CharField(default='no', max_length=50, verbose_name='COVIDU'),
        ),
        migrations.AddField(
            model_name='vacunaspacientes',
            name='FIEBRE_AMARILLA_1',
            field=models.CharField(default='no', max_length=50, verbose_name='FIEBREAMARILLA1'),
        ),
        migrations.AddField(
            model_name='vacunaspacientes',
            name='FIEBRE_AMARILLA_2',
            field=models.CharField(default='no', max_length=50, verbose_name='FIEBREAMARILLA2'),
        ),
        migrations.AddField(
            model_name='vacunaspacientes',
            name='FIEBRE_AMARILLA_3',
            field=models.CharField(default='no', max_length=50, verbose_name='FIEBREAMARILLA3'),
        ),
        migrations.AddField(
            model_name='vacunaspacientes',
            name='FIEBRE_AMARILLA_4',
            field=models.CharField(default='no', max_length=50, verbose_name='FIEBREAMARILLA4'),
        ),
        migrations.AddField(
            model_name='vacunaspacientes',
            name='FIEBRE_AMARILLA_5',
            field=models.CharField(default='no', max_length=50, verbose_name='FIEBREAMARILLA5'),
        ),
        migrations.AddField(
            model_name='vacunaspacientes',
            name='FIEBRE_AMARILLA_R1',
            field=models.CharField(default='no', max_length=50, verbose_name='FIEBREAMARILLAR1'),
        ),
        migrations.AddField(
            model_name='vacunaspacientes',
            name='FIEBRE_AMARILLA_R2',
            field=models.CharField(default='no', max_length=50, verbose_name='FIEBREAMARILLAR2'),
        ),
        migrations.AddField(
            model_name='vacunaspacientes',
            name='FIEBRE_AMARILLA_R3',
            field=models.CharField(default='no', max_length=50, verbose_name='FIEBREAMARILLAR3'),
        ),
        migrations.AddField(
            model_name='vacunaspacientes',
            name='FIEBRE_AMARILLA_U',
            field=models.CharField(default='no', max_length=50, verbose_name='FIEBREAMARILLAU'),
        ),
        migrations.AddField(
            model_name='vacunaspacientes',
            name='FIEBRE_TIFOIDEA_1',
            field=models.CharField(default='no', max_length=50, verbose_name='FIEBRETIFOIDEA1'),
        ),
        migrations.AddField(
            model_name='vacunaspacientes',
            name='FIEBRE_TIFOIDEA_2',
            field=models.CharField(default='no', max_length=50, verbose_name='FIEBRETIFOIDEA2'),
        ),
        migrations.AddField(
            model_name='vacunaspacientes',
            name='FIEBRE_TIFOIDEA_3',
            field=models.CharField(default='no', max_length=50, verbose_name='FIEBRETIFOIDEA3'),
        ),
        migrations.AddField(
            model_name='vacunaspacientes',
            name='FIEBRE_TIFOIDEA_4',
            field=models.CharField(default='no', max_length=50, verbose_name='FIEBRETIFOIDEA4'),
        ),
        migrations.AddField(
            model_name='vacunaspacientes',
            name='FIEBRE_TIFOIDEA_5',
            field=models.CharField(default='no', max_length=50, verbose_name='FIEBRETIFOIDEA5'),
        ),
        migrations.AddField(
            model_name='vacunaspacientes',
            name='FIEBRE_TIFOIDEA_R1',
            field=models.CharField(default='no', max_length=50, verbose_name='FIEBRETIFOIDEAR1'),
        ),
        migrations.AddField(
            model_name='vacunaspacientes',
            name='FIEBRE_TIFOIDEA_R2',
            field=models.CharField(default='no', max_length=50, verbose_name='FIEBRETIFOIDEAR2'),
        ),
        migrations.AddField(
            model_name='vacunaspacientes',
            name='FIEBRE_TIFOIDEA_R3',
            field=models.CharField(default='no', max_length=50, verbose_name='FIEBRETIFOIDEAR3'),
        ),
        migrations.AddField(
            model_name='vacunaspacientes',
            name='FIEBRE_TIFOIDEA_U',
            field=models.CharField(default='no', max_length=50, verbose_name='FIEBRETIFOIDEAU'),
        ),
        migrations.AddField(
            model_name='vacunaspacientes',
            name='HA_HB_1',
            field=models.CharField(default='no', max_length=50, verbose_name='HAHB1'),
        ),
        migrations.AddField(
            model_name='vacunaspacientes',
            name='HA_HB_2',
            field=models.CharField(default='no', max_length=50, verbose_name='HAHB2'),
        ),
        migrations.AddField(
            model_name='vacunaspacientes',
            name='HA_HB_3',
            field=models.CharField(default='no', max_length=50, verbose_name='HAHB3'),
        ),
        migrations.AddField(
            model_name='vacunaspacientes',
            name='HA_HB_4',
            field=models.CharField(default='no', max_length=50, verbose_name='HAHB4'),
        ),
        migrations.AddField(
            model_name='vacunaspacientes',
            name='HA_HB_5',
            field=models.CharField(default='no', max_length=50, verbose_name='HAHB5'),
        ),
        migrations.AddField(
            model_name='vacunaspacientes',
            name='HA_HB_R1',
            field=models.CharField(default='no', max_length=50, verbose_name='HAHBR1'),
        ),
        migrations.AddField(
            model_name='vacunaspacientes',
            name='HA_HB_R2',
            field=models.CharField(default='no', max_length=50, verbose_name='HAHBR2'),
        ),
        migrations.AddField(
            model_name='vacunaspacientes',
            name='HA_HB_R3',
            field=models.CharField(default='no', max_length=50, verbose_name='HAHBR3'),
        ),
        migrations.AddField(
            model_name='vacunaspacientes',
            name='HA_HB_U',
            field=models.CharField(default='no', max_length=50, verbose_name='HAHBU'),
        ),
        migrations.AddField(
            model_name='vacunaspacientes',
            name='HEPATITIS_A_1',
            field=models.CharField(default='no', max_length=50, verbose_name='HA1'),
        ),
        migrations.AddField(
            model_name='vacunaspacientes',
            name='HEPATITIS_A_2',
            field=models.CharField(default='no', max_length=50, verbose_name='HA2'),
        ),
        migrations.AddField(
            model_name='vacunaspacientes',
            name='HEPATITIS_A_3',
            field=models.CharField(default='no', max_length=50, verbose_name='HA3'),
        ),
        migrations.AddField(
            model_name='vacunaspacientes',
            name='HEPATITIS_A_4',
            field=models.CharField(default='no', max_length=50, verbose_name='HA4'),
        ),
        migrations.AddField(
            model_name='vacunaspacientes',
            name='HEPATITIS_A_5',
            field=models.CharField(default='no', max_length=50, verbose_name='HA5'),
        ),
        migrations.AddField(
            model_name='vacunaspacientes',
            name='HEPATITIS_A_R1',
            field=models.CharField(default='no', max_length=50, verbose_name='HAR1'),
        ),
        migrations.AddField(
            model_name='vacunaspacientes',
            name='HEPATITIS_A_R2',
            field=models.CharField(default='no', max_length=50, verbose_name='HAR2'),
        ),
        migrations.AddField(
            model_name='vacunaspacientes',
            name='HEPATITIS_A_R3',
            field=models.CharField(default='no', max_length=50, verbose_name='HAR3'),
        ),
        migrations.AddField(
            model_name='vacunaspacientes',
            name='HEPATITIS_A_U',
            field=models.CharField(default='no', max_length=50, verbose_name='HAU'),
        ),
        migrations.AddField(
            model_name='vacunaspacientes',
            name='HEPATITIS_B_1',
            field=models.CharField(default='no', max_length=50, verbose_name='HB1'),
        ),
        migrations.AddField(
            model_name='vacunaspacientes',
            name='HEPATITIS_B_2',
            field=models.CharField(default='no', max_length=50, verbose_name='HB2'),
        ),
        migrations.AddField(
            model_name='vacunaspacientes',
            name='HEPATITIS_B_3',
            field=models.CharField(default='no', max_length=50, verbose_name='HB3'),
        ),
        migrations.AddField(
            model_name='vacunaspacientes',
            name='HEPATITIS_B_4',
            field=models.CharField(default='no', max_length=50, verbose_name='HB4'),
        ),
        migrations.AddField(
            model_name='vacunaspacientes',
            name='HEPATITIS_B_5',
            field=models.CharField(default='no', max_length=50, verbose_name='HB5'),
        ),
        migrations.AddField(
            model_name='vacunaspacientes',
            name='HEPATITIS_B_R1',
            field=models.CharField(default='no', max_length=50, verbose_name='HBR1'),
        ),
        migrations.AddField(
            model_name='vacunaspacientes',
            name='HEPATITIS_B_R2',
            field=models.CharField(default='no', max_length=50, verbose_name='HBR2'),
        ),
        migrations.AddField(
            model_name='vacunaspacientes',
            name='HEPATITIS_B_R3',
            field=models.CharField(default='no', max_length=50, verbose_name='HBR3'),
        ),
        migrations.AddField(
            model_name='vacunaspacientes',
            name='HEPATITIS_B_U',
            field=models.CharField(default='no', max_length=50, verbose_name='HBU'),
        ),
        migrations.AddField(
            model_name='vacunaspacientes',
            name='HERPES_ZOSTER_1',
            field=models.CharField(default='no', max_length=50, verbose_name='HERPES1'),
        ),
        migrations.AddField(
            model_name='vacunaspacientes',
            name='HERPES_ZOSTER_2',
            field=models.CharField(default='no', max_length=50, verbose_name='HERPES2'),
        ),
        migrations.AddField(
            model_name='vacunaspacientes',
            name='HERPES_ZOSTER_3',
            field=models.CharField(default='no', max_length=50, verbose_name='HERPES3'),
        ),
        migrations.AddField(
            model_name='vacunaspacientes',
            name='HERPES_ZOSTER_4',
            field=models.CharField(default='no', max_length=50, verbose_name='HERPES4'),
        ),
        migrations.AddField(
            model_name='vacunaspacientes',
            name='HERPES_ZOSTER_5',
            field=models.CharField(default='no', max_length=50, verbose_name='HERPES5'),
        ),
        migrations.AddField(
            model_name='vacunaspacientes',
            name='HERPES_ZOSTER_R1',
            field=models.CharField(default='no', max_length=50, verbose_name='HERPESR1'),
        ),
        migrations.AddField(
            model_name='vacunaspacientes',
            name='HERPES_ZOSTER_R2',
            field=models.CharField(default='no', max_length=50, verbose_name='HERPESR2'),
        ),
        migrations.AddField(
            model_name='vacunaspacientes',
            name='HERPES_ZOSTER_R3',
            field=models.CharField(default='no', max_length=50, verbose_name='HERPESR3'),
        ),
        migrations.AddField(
            model_name='vacunaspacientes',
            name='HERPES_ZOSTER_U',
            field=models.CharField(default='no', max_length=50, verbose_name='HERPESU'),
        ),
        migrations.AddField(
            model_name='vacunaspacientes',
            name='INFLUENZA_1',
            field=models.CharField(default='no', max_length=50, verbose_name='INFLUENZA1'),
        ),
        migrations.AddField(
            model_name='vacunaspacientes',
            name='INFLUENZA_2',
            field=models.CharField(default='no', max_length=50, verbose_name='INFLUENZA2'),
        ),
        migrations.AddField(
            model_name='vacunaspacientes',
            name='INFLUENZA_3',
            field=models.CharField(default='no', max_length=50, verbose_name='INFLUENZA3'),
        ),
        migrations.AddField(
            model_name='vacunaspacientes',
            name='INFLUENZA_4',
            field=models.CharField(default='no', max_length=50, verbose_name='INFLUENZA4'),
        ),
        migrations.AddField(
            model_name='vacunaspacientes',
            name='INFLUENZA_5',
            field=models.CharField(default='no', max_length=50, verbose_name='INFLUENZA5'),
        ),
        migrations.AddField(
            model_name='vacunaspacientes',
            name='INFLUENZA_R1',
            field=models.CharField(default='no', max_length=50, verbose_name='INFLUENZAR1'),
        ),
        migrations.AddField(
            model_name='vacunaspacientes',
            name='INFLUENZA_R2',
            field=models.CharField(default='no', max_length=50, verbose_name='INFLUENZAR2'),
        ),
        migrations.AddField(
            model_name='vacunaspacientes',
            name='INFLUENZA_R3',
            field=models.CharField(default='no', max_length=50, verbose_name='INFLUENZAR3'),
        ),
        migrations.AddField(
            model_name='vacunaspacientes',
            name='INFLUENZA_U',
            field=models.CharField(default='no', max_length=50, verbose_name='INFLUENZAU'),
        ),
        migrations.AddField(
            model_name='vacunaspacientes',
            name='MENINGOCOCO_1',
            field=models.CharField(default='no', max_length=50, verbose_name='MENINGO1'),
        ),
        migrations.AddField(
            model_name='vacunaspacientes',
            name='MENINGOCOCO_2',
            field=models.CharField(default='no', max_length=50, verbose_name='MENINGO2'),
        ),
        migrations.AddField(
            model_name='vacunaspacientes',
            name='MENINGOCOCO_3',
            field=models.CharField(default='no', max_length=50, verbose_name='MENINGO3'),
        ),
        migrations.AddField(
            model_name='vacunaspacientes',
            name='MENINGOCOCO_4',
            field=models.CharField(default='no', max_length=50, verbose_name='MENINGO4'),
        ),
        migrations.AddField(
            model_name='vacunaspacientes',
            name='MENINGOCOCO_5',
            field=models.CharField(default='no', max_length=50, verbose_name='MENINGO5'),
        ),
        migrations.AddField(
            model_name='vacunaspacientes',
            name='MENINGOCOCO_R1',
            field=models.CharField(default='no', max_length=50, verbose_name='MENINGOR1'),
        ),
        migrations.AddField(
            model_name='vacunaspacientes',
            name='MENINGOCOCO_R2',
            field=models.CharField(default='no', max_length=50, verbose_name='MENINGOR2'),
        ),
        migrations.AddField(
            model_name='vacunaspacientes',
            name='MENINGOCOCO_R3',
            field=models.CharField(default='no', max_length=50, verbose_name='MENINGOR3'),
        ),
        migrations.AddField(
            model_name='vacunaspacientes',
            name='MENINGOCOCO_U',
            field=models.CharField(default='no', max_length=50, verbose_name='MENINGOU'),
        ),
        migrations.AddField(
            model_name='vacunaspacientes',
            name='TETANO_ANTITETANICA_1',
            field=models.CharField(default='no', max_length=50, verbose_name='TETANO1'),
        ),
        migrations.AddField(
            model_name='vacunaspacientes',
            name='TETANO_ANTITETANICA_2',
            field=models.CharField(default='no', max_length=50, verbose_name='TETANO2'),
        ),
        migrations.AddField(
            model_name='vacunaspacientes',
            name='TETANO_ANTITETANICA_3',
            field=models.CharField(default='no', max_length=50, verbose_name='TETANO3'),
        ),
        migrations.AddField(
            model_name='vacunaspacientes',
            name='TETANO_ANTITETANICA_4',
            field=models.CharField(default='no', max_length=50, verbose_name='TETANO4'),
        ),
        migrations.AddField(
            model_name='vacunaspacientes',
            name='TETANO_ANTITETANICA_5',
            field=models.CharField(default='no', max_length=50, verbose_name='TETANO5'),
        ),
        migrations.AddField(
            model_name='vacunaspacientes',
            name='TETANO_ANTITETANICA_R1',
            field=models.CharField(default='no', max_length=50, verbose_name='TETANOR1'),
        ),
        migrations.AddField(
            model_name='vacunaspacientes',
            name='TETANO_ANTITETANICA_R2',
            field=models.CharField(default='no', max_length=50, verbose_name='TETANOR2'),
        ),
        migrations.AddField(
            model_name='vacunaspacientes',
            name='TETANO_ANTITETANICA_R3',
            field=models.CharField(default='no', max_length=50, verbose_name='TETANOR3'),
        ),
        migrations.AddField(
            model_name='vacunaspacientes',
            name='TETANO_ANTITETANICA_U',
            field=models.CharField(default='no', max_length=50, verbose_name='TETANOU'),
        ),
        migrations.AddField(
            model_name='vacunaspacientes',
            name='TETANO_DIFTERICO_1',
            field=models.CharField(default='no', max_length=50, verbose_name='TETANODIFTERICO1'),
        ),
        migrations.AddField(
            model_name='vacunaspacientes',
            name='TETANO_DIFTERICO_2',
            field=models.CharField(default='no', max_length=50, verbose_name='TETANODIFTERICO2'),
        ),
        migrations.AddField(
            model_name='vacunaspacientes',
            name='TETANO_DIFTERICO_3',
            field=models.CharField(default='no', max_length=50, verbose_name='TETANODIFTERICO3'),
        ),
        migrations.AddField(
            model_name='vacunaspacientes',
            name='TETANO_DIFTERICO_4',
            field=models.CharField(default='no', max_length=50, verbose_name='TETANODIFTERICO4'),
        ),
        migrations.AddField(
            model_name='vacunaspacientes',
            name='TETANO_DIFTERICO_5',
            field=models.CharField(default='no', max_length=50, verbose_name='TETANODIFTERICO5'),
        ),
        migrations.AddField(
            model_name='vacunaspacientes',
            name='TETANO_DIFTERICO_R1',
            field=models.CharField(default='no', max_length=50, verbose_name='TETANODIFTERICOR1'),
        ),
        migrations.AddField(
            model_name='vacunaspacientes',
            name='TETANO_DIFTERICO_R2',
            field=models.CharField(default='no', max_length=50, verbose_name='TETANODIFTERICOR2'),
        ),
        migrations.AddField(
            model_name='vacunaspacientes',
            name='TETANO_DIFTERICO_R3',
            field=models.CharField(default='no', max_length=50, verbose_name='TETANODIFTERICOR3'),
        ),
        migrations.AddField(
            model_name='vacunaspacientes',
            name='TETANO_DIFTERICO_U',
            field=models.CharField(default='no', max_length=50, verbose_name='TETANODIFTERICOU'),
        ),
        migrations.AddField(
            model_name='vacunaspacientes',
            name='TRIPLE_VIRAL_1',
            field=models.CharField(default='no', max_length=50, verbose_name='TRIPLEVIRAL1'),
        ),
        migrations.AddField(
            model_name='vacunaspacientes',
            name='TRIPLE_VIRAL_2',
            field=models.CharField(default='no', max_length=50, verbose_name='TRIPLEVIRAL2'),
        ),
        migrations.AddField(
            model_name='vacunaspacientes',
            name='TRIPLE_VIRAL_3',
            field=models.CharField(default='no', max_length=50, verbose_name='TRIPLEVIRAL3'),
        ),
        migrations.AddField(
            model_name='vacunaspacientes',
            name='TRIPLE_VIRAL_4',
            field=models.CharField(default='no', max_length=50, verbose_name='TRIPLEVIRAL4'),
        ),
        migrations.AddField(
            model_name='vacunaspacientes',
            name='TRIPLE_VIRAL_5',
            field=models.CharField(default='no', max_length=50, verbose_name='TRIPLEVIRAL5'),
        ),
        migrations.AddField(
            model_name='vacunaspacientes',
            name='TRIPLE_VIRAL_R1',
            field=models.CharField(default='no', max_length=50, verbose_name='TRIPLEVIRALR1'),
        ),
        migrations.AddField(
            model_name='vacunaspacientes',
            name='TRIPLE_VIRAL_R2',
            field=models.CharField(default='no', max_length=50, verbose_name='TRIPLEVIRALR2'),
        ),
        migrations.AddField(
            model_name='vacunaspacientes',
            name='TRIPLE_VIRAL_R3',
            field=models.CharField(default='no', max_length=50, verbose_name='TRIPLEVIRALR3'),
        ),
        migrations.AddField(
            model_name='vacunaspacientes',
            name='TRIPLE_VIRAL_U',
            field=models.CharField(default='no', max_length=50, verbose_name='TRIPLEVIRALU'),
        ),
        migrations.AddField(
            model_name='vacunaspacientes',
            name='VARICELA_1',
            field=models.CharField(default='no', max_length=50, verbose_name='VARICELA1'),
        ),
        migrations.AddField(
            model_name='vacunaspacientes',
            name='VARICELA_2',
            field=models.CharField(default='no', max_length=50, verbose_name='VARICELA2'),
        ),
        migrations.AddField(
            model_name='vacunaspacientes',
            name='VARICELA_3',
            field=models.CharField(default='no', max_length=50, verbose_name='VARICELA3'),
        ),
        migrations.AddField(
            model_name='vacunaspacientes',
            name='VARICELA_4',
            field=models.CharField(default='no', max_length=50, verbose_name='VARICELA4'),
        ),
        migrations.AddField(
            model_name='vacunaspacientes',
            name='VARICELA_5',
            field=models.CharField(default='no', max_length=50, verbose_name='VARICELA5'),
        ),
        migrations.AddField(
            model_name='vacunaspacientes',
            name='VARICELA_R1',
            field=models.CharField(default='no', max_length=50, verbose_name='VARICELAR1'),
        ),
        migrations.AddField(
            model_name='vacunaspacientes',
            name='VARICELA_R2',
            field=models.CharField(default='no', max_length=50, verbose_name='VARICELAR2'),
        ),
        migrations.AddField(
            model_name='vacunaspacientes',
            name='VARICELA_R3',
            field=models.CharField(default='no', max_length=50, verbose_name='VARICELAR3'),
        ),
        migrations.AddField(
            model_name='vacunaspacientes',
            name='VARICELA_U',
            field=models.CharField(default='no', max_length=50, verbose_name='VARICELAU'),
        ),
        migrations.AddField(
            model_name='vacunaspacientes',
            name='VPH_1',
            field=models.CharField(default='no', max_length=50, verbose_name='VPH1'),
        ),
        migrations.AddField(
            model_name='vacunaspacientes',
            name='VPH_2',
            field=models.CharField(default='no', max_length=50, verbose_name='VPH2'),
        ),
        migrations.AddField(
            model_name='vacunaspacientes',
            name='VPH_3',
            field=models.CharField(default='no', max_length=50, verbose_name='VPH3'),
        ),
        migrations.AddField(
            model_name='vacunaspacientes',
            name='VPH_4',
            field=models.CharField(default='no', max_length=50, verbose_name='VPH4'),
        ),
        migrations.AddField(
            model_name='vacunaspacientes',
            name='VPH_5',
            field=models.CharField(default='no', max_length=50, verbose_name='VPH5'),
        ),
        migrations.AddField(
            model_name='vacunaspacientes',
            name='VPH_R1',
            field=models.CharField(default='no', max_length=50, verbose_name='VPHR1'),
        ),
        migrations.AddField(
            model_name='vacunaspacientes',
            name='VPH_R2',
            field=models.CharField(default='no', max_length=50, verbose_name='VPHR2'),
        ),
        migrations.AddField(
            model_name='vacunaspacientes',
            name='VPH_R3',
            field=models.CharField(default='no', max_length=50, verbose_name='VPHR3'),
        ),
        migrations.AddField(
            model_name='vacunaspacientes',
            name='VPH_U',
            field=models.CharField(default='no', max_length=50, verbose_name='VPHU'),
        ),
    ]
