# Generated by Django 2.0.6 on 2019-01-03 13:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0015_auto_20181217_1711'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='Financial_Year_From',
            field=models.DateField(choices=[(datetime.date(2019, 4, 1), datetime.date(2019, 4, 1)), (datetime.date(2019, 1, 1), datetime.date(2019, 1, 1))], default=datetime.date(2019, 4, 1)),
        ),
    ]
