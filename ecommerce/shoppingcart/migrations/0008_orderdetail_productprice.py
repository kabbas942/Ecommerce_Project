# Generated by Django 4.2.1 on 2023-05-20 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoppingcart', '0007_orderdetail_orderproductquantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderdetail',
            name='productPrice',
            field=models.IntegerField(default=0),
        ),
    ]
