# Generated by Django 3.1.2 on 2020-12-09 10:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0011_auto_20201209_1632'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='description1',
        ),
        migrations.RemoveField(
            model_name='product',
            name='description2',
        ),
    ]
