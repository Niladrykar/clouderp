# Generated by Django 2.0.6 on 2018-12-17 11:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0014_auto_20181103_1407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='Financial_Year_From',
            field=models.DateField(choices=[(datetime.date(2018, 4, 1), datetime.date(2018, 4, 1)), (datetime.date(2018, 1, 1), datetime.date(2018, 1, 1))], default=datetime.date(2018, 4, 1)),
        ),
    ]