# Generated by Django 2.0.6 on 2018-10-29 12:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0010_auto_20181025_1917'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='Books_Begining_From',
            field=models.DateField(default=datetime.date(2018, 4, 1)),
        ),
        migrations.AlterField(
            model_name='company',
            name='Financial_Year_From',
            field=models.DateField(default=datetime.date(2018, 4, 1)),
        ),
    ]
