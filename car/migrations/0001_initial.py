# Generated by Django 4.2.3 on 2023-09-01 14:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('brand', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('description', models.TextField(blank=True, max_length=1000)),
                ('price', models.IntegerField()),
                ('images', models.ImageField(upload_to='photos/cars')),
                ('color', models.CharField(max_length=50)),
                ('model', models.CharField(max_length=50)),
                ('is_available', models.BooleanField(default=True)),
                ('features', models.TextField(blank=True, max_length=500)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='brand.brand')),
            ],
        ),
    ]