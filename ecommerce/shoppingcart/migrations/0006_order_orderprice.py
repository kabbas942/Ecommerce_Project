# Generated by Django 4.2.1 on 2023-05-19 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoppingcart', '0005_order_orderdetail'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='orderPrice',
            field=models.IntegerField(default=0),
        ),
    ]
