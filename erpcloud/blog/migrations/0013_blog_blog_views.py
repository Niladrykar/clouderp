# Generated by Django 2.0.6 on 2018-09-20 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20180920_1802'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='blog_views',
            field=models.IntegerField(default=0),
        ),
    ]
