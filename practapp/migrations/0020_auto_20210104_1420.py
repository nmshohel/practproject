# Generated by Django 3.1.4 on 2021-01-04 14:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('practapp', '0019_auto_20210104_1415'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='catogey',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='practapp.catogery'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='catogery',
            name='name',
            field=models.CharField(max_length=250),
        ),
    ]
