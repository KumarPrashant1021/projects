# Generated by Django 3.0.6 on 2020-06-23 12:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('old', '0018_auto_20200623_1815'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='user_id',
        ),
    ]
