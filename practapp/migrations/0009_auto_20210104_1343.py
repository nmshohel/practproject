# Generated by Django 3.1.4 on 2021-01-04 13:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('practapp', '0008_auto_20210104_1340'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
