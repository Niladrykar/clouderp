# Generated by Django 2.0.6 on 2018-09-26 11:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_remove_blog_counter'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ['-id']},
        ),
    ]
