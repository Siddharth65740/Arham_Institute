# Generated by Django 3.1.7 on 2021-05-02 03:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inquiry_table', '0008_auto_20210501_1604'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inquiry',
            name='inq_id',
        ),
    ]