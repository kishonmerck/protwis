# Generated by Django 2.0.8 on 2019-06-05 09:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('protein', '0007_proteingproteinpair_references'),
        ('residue', '0002_auto_20180504_1417'),
        ('structure', '0017_structure_contact_representative_score'),
        ('contactnetwork', '0008_auto_20190605_1054'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='consensus_interactions',
            new_name='ConsensusInteractions',
        ),
    ]
