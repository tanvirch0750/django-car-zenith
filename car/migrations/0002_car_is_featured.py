# Generated by Django 4.2.3 on 2023-09-01 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='is_featured',
            field=models.BooleanField(default=False),
        ),
    ]