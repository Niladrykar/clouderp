# Generated by Django 2.0.6 on 2018-10-02 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounting_double_entry', '0005_auto_20180928_1219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group1',
            name='group_Name',
            field=models.CharField(max_length=32),
        ),
    ]