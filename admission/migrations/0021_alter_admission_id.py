# Generated by Django 3.2.3 on 2022-02-20 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admission', '0020_auto_20210503_0952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admission',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
