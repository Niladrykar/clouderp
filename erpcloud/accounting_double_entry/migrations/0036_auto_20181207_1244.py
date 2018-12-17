# Generated by Django 2.0.6 on 2018-12-07 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounting_double_entry', '0035_ledger1_closing_balance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ledger1',
            name='Closing_balance',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10),
        ),
    ]