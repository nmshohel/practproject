# Generated by Django 3.1.4 on 2021-01-02 17:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('practapp', '0005_discrict'),
    ]

    operations = [
        migrations.AddField(
            model_name='discrict',
            name='division',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='practapp.division'),
            preserve_default=False,
        ),
    ]