# Generated by Django 4.1.7 on 2023-03-28 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='mymessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=200)),
                ('mobile', models.CharField(max_length=200)),
                ('company', models.CharField(max_length=200)),
                ('message', models.TextField(max_length=500)),
                ('date', models.DateField()),
            ],
        ),
    ]