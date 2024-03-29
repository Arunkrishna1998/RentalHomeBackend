# Generated by Django 5.0 on 2024-02-14 07:55

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ChatMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=1000)),
                ('is_read', models.BooleanField(default=False)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('reciever', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='reciever', to=settings.AUTH_USER_MODEL)),
                ('sender', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sender', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(max_length=200, unique=True)),
                ('title', models.CharField(max_length=150)),
                ('address', models.CharField(max_length=150)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('zipcode', models.CharField(max_length=15)),
                ('description', models.TextField(blank=True)),
                ('sale_type', models.CharField(choices=[('For Sale', 'For Sale'), ('For Rent', 'For Rent')], default='For Sale', max_length=50)),
                ('price', models.IntegerField()),
                ('bedrooms', models.IntegerField()),
                ('bathrooms', models.DecimalField(decimal_places=1, max_digits=2)),
                ('home_type', models.CharField(choices=[('House', 'House'), ('Condo', 'Condo'), ('Townhouse', 'Townhouse')], default='House', max_length=50)),
                ('sqft', models.IntegerField()),
                ('open_house', models.BooleanField(default=False)),
                ('photo_main', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('photo_1', models.ImageField(blank=True, null=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_2', models.ImageField(blank=True, null=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_3', models.ImageField(blank=True, null=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_4', models.ImageField(blank=True, null=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_5', models.ImageField(blank=True, null=True, upload_to='photos/%Y/%m/%d/')),
                ('is_published', models.BooleanField(default=True)),
                ('list_date', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('realtor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Notifications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('send_time', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('is_seen', models.BooleanField(default=False)),
                ('fromuser', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sent_notifications', to=settings.AUTH_USER_MODEL)),
                ('intrested_post', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='listings.listing')),
                ('touser', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='received_notifications', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
