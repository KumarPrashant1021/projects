# Generated by Django 3.0.6 on 2020-06-06 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('old', '0010_orderitem_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='quantity',
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
    ]