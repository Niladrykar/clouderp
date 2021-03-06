# Generated by Django 2.0.6 on 2018-10-12 13:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounting_double_entry', '0023_auto_20181012_1842'),
    ]

    operations = [
        migrations.AddField(
            model_name='journal',
            name='end_date',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='enddate', to='accounting_double_entry.selectdatefield'),
        ),
        migrations.AddField(
            model_name='journal',
            name='start_date',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='startdate', to='accounting_double_entry.selectdatefield'),
        ),
    ]
