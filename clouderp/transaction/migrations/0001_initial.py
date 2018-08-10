# Generated by Django 2.0.7 on 2018-08-03 13:42

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('double_entry', '0007_auto_20180801_1817'),
    ]

    operations = [
        migrations.CreateModel(
            name='journal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Creation_Date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('Credit', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Total_Amount_Credited', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='ledger1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Creation_Date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('name', models.CharField(max_length=32, unique=True)),
                ('Opening_Balance', models.DecimalField(decimal_places=4, max_digits=19)),
                ('Inventory_Values_are_affected', models.BooleanField(default=False)),
                ('User_Name', models.CharField(max_length=100)),
                ('Address', models.TextField()),
                ('State', models.CharField(choices=[('Choose', 'Choose'), ('Andra Pradesh', 'Andra Pradesh'), ('Arunachal Pradesh', 'Arunachal Pradesh'), ('Assam', 'Assam'), ('Bihar', 'Bihar'), ('Chhattisghar', 'Chhattisghar'), ('Goa', 'Goa'), ('Gujrat', 'Gujrat'), ('Haryana', 'Haryana'), ('Himachal Pradesh', 'Himachal Pradesh'), ('Jammu and Kashmir', 'Jammu and Kashmir'), ('Jharkhand', 'Jharkhand'), ('Karnataka', 'Karnataka'), ('Kerala', 'Kerala'), ('Madhya Pradesh', 'Madhya Pradesh'), ('Maharasthra', 'Maharasthra'), ('Manipur', 'Manipur'), ('Meghalaya', 'Meghalaya'), ('Mizoram', 'Mizoram'), ('Nagaland', 'Nagaland'), ('Odisha', 'Odisha'), ('Punjab', 'Punjab'), ('Rajasthan', 'Rajasthan'), ('Sikkim', 'Sikkim'), ('Tamil Nadu', 'Tamil Nadu'), ('Telengana', 'Telengana'), ('Tripura', 'Tripura'), ('Uttar Pradesh', 'Uttar Pradesh'), ('Uttarakhand', 'Uttarakhand'), ('West Bengal', 'West Bengal')], default='Choose', max_length=100)),
                ('Pin_Code', models.BigIntegerField()),
                ('PanIt_No', models.CharField(blank=True, max_length=100)),
                ('GST_No', models.CharField(blank=True, max_length=100)),
                ('group1_Name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='double_entry.group1')),
            ],
        ),
        migrations.CreateModel(
            name='transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Creation_Date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('Debit', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Total_Amount_Debited', models.DecimalField(decimal_places=2, max_digits=10)),
                ('By1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transaction.ledger1')),
            ],
        ),
        migrations.AddField(
            model_name='journal',
            name='To1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transaction.ledger1'),
        ),
    ]