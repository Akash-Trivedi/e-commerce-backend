# Generated by Django 4.0.3 on 2022-03-20 05:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('publisher', '0004_shop_sales'),
        ('customer', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='shopId',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='publisher.shop'),
            preserve_default=False,
        ),
    ]
