# Generated by Django 3.1.4 on 2021-01-02 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('practapp', '0004_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Discrict',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
        ),
    ]