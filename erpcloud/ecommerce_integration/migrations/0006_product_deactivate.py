# Generated by Django 2.0.6 on 2019-02-08 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce_integration', '0005_product_activate'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='deactivate',
            field=models.BooleanField(default=False),
        ),
    ]
