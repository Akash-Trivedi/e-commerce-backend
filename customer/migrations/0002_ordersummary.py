# Generated by Django 4.0.2 on 2022-02-22 17:15

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderSummary',
            fields=[
                ('orderId', models.AutoField(primary_key=True, serialize=False)),
                ('transactionId', models.CharField(max_length=255)),
                ('orderPlaceTime', models.DateTimeField(verbose_name=django.utils.timezone.now)),
                ('orderDispatchTime', models.DateTimeField(null=True)),
                ('orderShippedTime', models.DateTimeField(null=True)),
                ('orderDeliveryTime', models.DateTimeField(null=True)),
                ('paymentTime', models.DateTimeField(null=True)),
                ('status', models.CharField(default='placed', max_length=10)),
                ('pincode', models.IntegerField()),
                ('paymentOption', models.CharField(max_length=16)),
                ('paymentDone', models.BooleanField(default=False)),
                ('paymentGateway', models.CharField(max_length=64)),
                ('addressId', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='customer.address')),
                ('customerId', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='customer.customer')),
            ],
        ),
    ]
