# Generated by Django 3.2.3 on 2022-02-20 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0004_course_master_fees'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course_master',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
