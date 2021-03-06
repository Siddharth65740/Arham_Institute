# Generated by Django 3.1.7 on 2021-04-02 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('middle_name', models.CharField(max_length=50)),
                ('father_firstname', models.CharField(max_length=50)),
                ('father_second_name', models.CharField(max_length=50)),
                ('father_last_name', models.CharField(max_length=50)),
                ('Building_name', models.CharField(max_length=50)),
                ('state_name', models.CharField(max_length=50)),
                ('area_name', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('ph_number', models.CharField(max_length=11)),
                ('ph_number_house', models.CharField(max_length=11)),
                ('birthdate', models.DateField()),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10)),
                ('Schoolname', models.CharField(max_length=50)),
                ('education', models.CharField(max_length=50)),
                ('photo', models.ImageField(upload_to='Profile Pic')),
                ('email', models.EmailField(max_length=254)),
                ('inquiry_id', models.CharField(max_length=50)),
            ],
        ),
    ]
