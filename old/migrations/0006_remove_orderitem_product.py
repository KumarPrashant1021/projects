# Generated by Django 3.0.6 on 2020-06-04 14:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('old', '0005_auto_20200604_1937'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='product',
        ),
    ]
