# Generated by Django 2.0.7 on 2018-07-31 12:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='companyowner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AlterModelOptions(
            name='company',
            options={'ordering': ['Name']},
        ),
        migrations.AddField(
            model_name='companyowner',
            name='Company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Company_Name', to='company.company'),
        ),
        migrations.AddField(
            model_name='companyowner',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Company_Owner', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='companyowner',
            unique_together={('Company', 'user')},
        ),
    ]
