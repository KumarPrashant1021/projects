# Generated by Django 3.0.6 on 2020-06-23 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('old', '0029_auto_20200623_2037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
