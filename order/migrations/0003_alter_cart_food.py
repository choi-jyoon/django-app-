# Generated by Django 5.0.3 on 2024-04-18 06:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_alter_cart_food'),
        ('seller', '0002_food_img_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='food',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seller.food'),
        ),
    ]