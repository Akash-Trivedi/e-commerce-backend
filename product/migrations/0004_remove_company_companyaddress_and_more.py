# Generated by Django 4.0.2 on 2022-02-19 13:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_company_alter_tag_tagname'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='companyAddress',
        ),
        migrations.RemoveField(
            model_name='company',
            name='companyBaseLocation',
        ),
        migrations.RemoveField(
            model_name='company',
            name='companyZipcode',
        ),
    ]