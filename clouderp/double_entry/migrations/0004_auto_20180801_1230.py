# Generated by Django 2.0.7 on 2018-08-01 07:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('double_entry', '0003_auto_20180801_1221'),
    ]

    operations = [
        migrations.RenameField(
            model_name='group1',
            old_name='group1_Name',
            new_name='group_Name',
        ),
    ]