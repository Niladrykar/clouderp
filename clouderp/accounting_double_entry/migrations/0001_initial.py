# Generated by Django 2.0.7 on 2018-08-21 10:39

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='group1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_Name', models.CharField(max_length=32, unique=True)),
                ('Master', models.CharField(choices=[('Primary', 'Primary'), ('Fixed_Asset', 'Fixed_Asset'), ('Current_Assets', 'Current_Assets'), ('Liabilities', 'Liabilities'), ('Current_Liabilities', 'Current_Liabilities'), ('Capital', 'Capital'), ('Loans', 'Loans'), ('Income', 'Income'), ('Expenses', 'Expenses')], default='Primary', max_length=32)),
                ('Nature_of_group1', models.CharField(choices=[('Assets', 'Assets'), ('Expenses', 'Expenses'), ('Income', 'Income'), ('Liabilities', 'Liabilities'), ('Not Applicable', 'Not Applicable')], default='Assets', max_length=32)),
                ('balance_nature', models.CharField(choices=[('Debit', 'Debit'), ('Credit', 'Credit'), ('Not Applicable', 'Not Applicable')], default='Debit', max_length=32)),
                ('Group_behaves_like_a_Sub_Ledger', models.BooleanField(default=False)),
                ('Nett_Debit_or_Credit_Balances_for_Reporting', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='journal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Debit', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Credit', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounting_double_entry.group1')),
            ],
        ),
        migrations.CreateModel(
            name='ledger1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Creation_Date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('name', models.CharField(max_length=32, unique=True)),
                ('Opening_Balance', models.DecimalField(decimal_places=2, max_digits=19)),
                ('Inventory_Values_are_affected', models.BooleanField(default=False)),
                ('User_Name', models.CharField(max_length=100)),
                ('Address', models.TextField()),
                ('State', models.CharField(choices=[('Choose', 'Choose'), ('Andra Pradesh', 'Andra Pradesh'), ('Arunachal Pradesh', 'Arunachal Pradesh'), ('Assam', 'Assam'), ('Bihar', 'Bihar'), ('Chhattisghar', 'Chhattisghar'), ('Goa', 'Goa'), ('Gujrat', 'Gujrat'), ('Haryana', 'Haryana'), ('Himachal Pradesh', 'Himachal Pradesh'), ('Jammu and Kashmir', 'Jammu and Kashmir'), ('Jharkhand', 'Jharkhand'), ('Karnataka', 'Karnataka'), ('Kerala', 'Kerala'), ('Madhya Pradesh', 'Madhya Pradesh'), ('Maharasthra', 'Maharasthra'), ('Manipur', 'Manipur'), ('Meghalaya', 'Meghalaya'), ('Mizoram', 'Mizoram'), ('Nagaland', 'Nagaland'), ('Odisha', 'Odisha'), ('Punjab', 'Punjab'), ('Rajasthan', 'Rajasthan'), ('Sikkim', 'Sikkim'), ('Tamil Nadu', 'Tamil Nadu'), ('Telengana', 'Telengana'), ('Tripura', 'Tripura'), ('Uttar Pradesh', 'Uttar Pradesh'), ('Uttarakhand', 'Uttarakhand'), ('West Bengal', 'West Bengal')], default='Choose', max_length=100)),
                ('Pin_Code', models.BigIntegerField()),
                ('PanIt_No', models.CharField(blank=True, max_length=100)),
                ('GST_No', models.CharField(blank=True, max_length=100)),
                ('group1_Name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounting_double_entry.group1')),
            ],
        ),
        migrations.AddField(
            model_name='journal',
            name='Particulars',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounting_double_entry.ledger1'),
        ),
        migrations.AddField(
            model_name='journal',
            name='Particulars_Credit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Creditledgers', to='accounting_double_entry.ledger1'),
        ),
    ]