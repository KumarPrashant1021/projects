# Generated by Django 3.0.6 on 2020-06-23 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('old', '0016_auto_20200623_1813'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='user_id',
            field=models.CharField(max_length=200, null=True),
        ),
    ]