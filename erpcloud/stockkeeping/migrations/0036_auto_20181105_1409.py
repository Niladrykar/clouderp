# Generated by Django 2.0.6 on 2018-11-05 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stockkeeping', '0035_stockdata_total_qty'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stock_total',
            old_name='Disc',
            new_name='Disc_p',
        ),
        migrations.RenameField(
            model_name='stock_total',
            old_name='Quantity',
            new_name='Quantity_p',
        ),
        migrations.RenameField(
            model_name='stock_total',
            old_name='Total',
            new_name='Total_p',
        ),
        migrations.RenameField(
            model_name='stock_total',
            old_name='gst_rate',
            new_name='gst_rate_p',
        ),
        migrations.RenameField(
            model_name='stock_total',
            old_name='rate',
            new_name='rate_p',
        ),
        migrations.RemoveField(
            model_name='stockdata',
            name='stock_date',
        ),
        migrations.AddField(
            model_name='stockdata',
            name='Total_P',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='stockdata',
            name='Total_S',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='stockdata',
            name='Total_SP',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='stockdata',
            name='qty_purchas',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='stockdata',
            name='qty_sale',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='sales',
            name='Address',
            field=models.CharField(blank=True, max_length=32),
        ),
    ]
