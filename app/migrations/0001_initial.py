# Generated by Django 2.2.10 on 2021-07-28 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='closest_point',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('points', models.CharField(max_length=100)),
                ('closest_points_pair', models.CharField(max_length=100)),
                ('createdAt', models.DateField(auto_now_add=True)),
                ('updatedAt', models.DateField(auto_now=True)),
            ],
        ),
    ]
