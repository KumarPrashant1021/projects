# Generated by Django 3.0.6 on 2020-06-23 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('old', '0023_auto_20200623_1836'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seller',
            name='phone',
            field=models.CharField(max_length=200, null=True),
        ),
    ]