# Generated by Django 3.0.6 on 2020-06-04 14:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('old', '0006_remove_orderitem_product'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='seller_name',
            new_name='product_id',
        ),
    ]
