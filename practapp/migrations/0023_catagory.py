# Generated by Django 3.1.4 on 2021-01-04 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('practapp', '0022_auto_20210104_1428'),
    ]

    operations = [
        migrations.CreateModel(
            name='Catagory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
        ),
    ]