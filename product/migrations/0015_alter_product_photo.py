# Generated by Django 4.0.3 on 2022-04-01 17:00

from django.db import migrations, models
import product.models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0014_alter_product_photo_delete_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='photo',
            field=models.ImageField(default='F:/github/e-commerce/e-commerce-backend/media/product-images/photos/default.jpg', null=True, upload_to=product.models.setImageName),
        ),
    ]
