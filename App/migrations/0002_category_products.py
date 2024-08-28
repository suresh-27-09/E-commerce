# Generated by Django 5.1 on 2024-08-28 05:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('cid', models.AutoField(primary_key=True, serialize=False)),
                ('c_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('pid', models.AutoField(primary_key=True, serialize=False)),
                ('p_name', models.CharField(max_length=255)),
                ('p_price', models.FloatField()),
                ('p_img', models.ImageField(upload_to='images/')),
                ('p_des', models.TextField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.category')),
            ],
        ),
    ]
