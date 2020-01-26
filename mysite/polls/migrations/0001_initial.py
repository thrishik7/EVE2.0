# Generated by Django 2.2.6 on 2020-01-25 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='feedback1_routes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('route_name', models.CharField(max_length=200)),
                ('illumination', models.FloatField()),
                ('overall_safety', models.FloatField()),
                ('road_condition', models.FloatField()),
                ('hazardous_contruction', models.FloatField()),
                ('no_of_reviews', models.FloatField()),
            ],
            options={
                'db_table': 'feedback1_routes',
            },
        ),
        migrations.CreateModel(
            name='feedback1_text',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('route_name', models.CharField(max_length=200)),
                ('review_text', models.CharField(max_length=300)),
            ],
            options={
                'db_table': 'feedback1_text',
            },
        ),
        migrations.CreateModel(
            name='login_user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=15)),
            ],
            options={
                'db_table': 'Employee',
            },
        ),
        migrations.CreateModel(
            name='tag1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=200)),
                ('no_of_occurance', models.FloatField()),
            ],
            options={
                'db_table': 'tag1',
            },
        ),
    ]
