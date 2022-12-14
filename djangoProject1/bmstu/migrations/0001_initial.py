# Generated by Django 4.1.3 on 2022-11-21 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Departments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DepName', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'Departments',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Notes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Type', models.CharField(max_length=25)),
                ('Text', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'Notes',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Sub_Notes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'Sub_Notes',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Subjects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SubName', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'Subjects',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Login', models.CharField(max_length=50)),
                ('Password', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'Users',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Years',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Count', models.IntegerField(max_length=1)),
            ],
            options={
                'db_table': 'Years',
                'managed': False,
            },
        ),
    ]
