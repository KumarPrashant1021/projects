# Generated by Django 3.0.6 on 2020-06-23 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('old', '0013_product_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='user',
        ),
        migrations.AddField(
            model_name='product',
            name='user_id',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
