# Generated by Django 2.0.6 on 2019-02-04 13:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='API',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32)),
                ('price', models.DecimalField(decimal_places=2, default=10000.0, max_digits=10)),
                ('image', models.ImageField(blank=True, default='userprofile/comming soon.jpg', null=True, upload_to='api_images')),
                ('rating', models.DecimalField(decimal_places=2, default=4.5, max_digits=4)),
                ('summary', models.TextField(max_length=150, null=True)),
                ('description', models.TextField(null=True)),
                ('User', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='coupon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_code', models.CharField(max_length=32)),
                ('description', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32)),
                ('price', models.DecimalField(decimal_places=2, default=10000.0, max_digits=10)),
                ('image', models.ImageField(blank=True, default='userprofile/comming soon.jpg', null=True, upload_to='product_images')),
                ('rating', models.DecimalField(decimal_places=2, default=4.5, max_digits=4)),
                ('summary', models.TextField(max_length=150, null=True)),
                ('description', models.TextField(null=True)),
                ('User', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('coupons', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_coupons', to='ecommerce_integration.coupon')),
            ],
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32)),
                ('image', models.ImageField(blank=True, default='userprofile/comming soon.jpg', null=True, upload_to='service_images')),
                ('summary', models.TextField(max_length=150, null=True)),
                ('description', models.TextField(null=True)),
                ('User', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='api',
            name='coupons',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='api_coupons', to='ecommerce_integration.coupon'),
        ),
    ]
