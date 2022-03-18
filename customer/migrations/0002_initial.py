# Generated by Django 4.0.3 on 2022-03-17 21:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product', '0002_initial'),
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordersummary',
            name='id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='customer_order', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='feedback',
            name='id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='customer_feedback', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='feedback',
            name='productId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product'),
        ),
        migrations.AddField(
            model_name='address',
            name='id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_address', to=settings.AUTH_USER_MODEL),
        ),
    ]