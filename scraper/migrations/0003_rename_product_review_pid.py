# Generated by Django 5.0.3 on 2024-07-11 14:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scraper', '0002_remove_review_id_alter_review_product_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='product',
            new_name='PID',
        ),
    ]
