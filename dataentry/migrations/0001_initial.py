# Generated by Django 5.0.3 on 2024-03-23 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roll_num', models.CharField(max_length=9)),
                ('name', models.CharField(max_length=25)),
                ('age', models.IntegerField()),
            ],
        ),
    ]
