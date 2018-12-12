# Generated by Django 2.0.6 on 2018-12-08 11:07

from django.db import migrations, models
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('stockkeeping', '0042_auto_20181208_1621'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stockdata',
            name='man_date',
        ),
        migrations.AddField(
            model_name='stockdata',
            name='bar_code',
            field=sorl.thumbnail.fields.ImageField(blank=True, null=True, upload_to='stockmanagement'),
        ),
        migrations.AddField(
            model_name='stockdata',
            name='mnf_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='stockdata',
            name='batch_no',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='stockdata',
            name='exp_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
