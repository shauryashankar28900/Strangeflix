# Generated by Django 3.0.6 on 2020-09-30 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vid', '0004_auto_20200930_2059'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
