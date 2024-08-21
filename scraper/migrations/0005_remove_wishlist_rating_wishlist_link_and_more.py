# Generated by Django 5.0.3 on 2024-07-12 04:02

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scraper', '0004_review_id_alter_review_pid'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wishlist',
            name='rating',
        ),
        migrations.AddField(
            model_name='wishlist',
            name='link',
            field=models.URLField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='review',
            name='PID',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='review',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='wishlist',
            name='PID',
            field=models.CharField(default='unknown', max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='wishlist',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
