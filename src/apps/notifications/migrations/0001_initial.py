# Generated by Django 4.1 on 2023-09-21 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BroadcastNotification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default='2f2498d3-e807-48c6-aeff-fe5ea27567b7', editable=False, unique=True)),
                ('is_deleted', models.BooleanField(blank=True, default=False, editable=False, null=True)),
                ('deleted_at', models.DateTimeField(blank=True, editable=False, null=True, verbose_name='تاریخ حذف')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='تاریخ بروزرسانی')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت')),
                ('title', models.CharField(max_length=250)),
                ('message', models.TextField()),
                ('broadcast_on', models.DateTimeField()),
                ('status', models.CharField(max_length=8)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='NotificationMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default='2f2498d3-e807-48c6-aeff-fe5ea27567b7', editable=False, unique=True)),
                ('is_deleted', models.BooleanField(blank=True, default=False, editable=False, null=True)),
                ('deleted_at', models.DateTimeField(blank=True, editable=False, null=True, verbose_name='تاریخ حذف')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='تاریخ بروزرسانی')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت')),
                ('message', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PrivateNotification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default='2f2498d3-e807-48c6-aeff-fe5ea27567b7', editable=False, unique=True)),
                ('is_deleted', models.BooleanField(blank=True, default=False, editable=False, null=True)),
                ('deleted_at', models.DateTimeField(blank=True, editable=False, null=True, verbose_name='تاریخ حذف')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='تاریخ بروزرسانی')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت')),
                ('message', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
