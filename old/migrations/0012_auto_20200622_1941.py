# Generated by Django 3.0.6 on 2020-06-22 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('old', '0011_auto_20200606_1221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seller',
            name='phone',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]