# Generated by Django 3.0.6 on 2020-10-07 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vid', '0012_auto_20201007_1010'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detail',
            name='intid',
        ),
        migrations.AddField(
            model_name='detail',
            name='vid',
            field=models.FileField(null=True, upload_to='videos'),
        ),
    ]
