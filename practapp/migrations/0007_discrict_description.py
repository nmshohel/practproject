# Generated by Django 3.1.4 on 2021-01-03 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('practapp', '0006_discrict_division'),
    ]

    operations = [
        migrations.AddField(
            model_name='discrict',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
