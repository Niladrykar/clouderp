# Generated by Django 2.0.6 on 2018-10-12 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounting_double_entry', '0021_auto_20181012_1140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ledger1',
            name='Creation_Date',
            field=models.DateField(),
        ),
    ]
