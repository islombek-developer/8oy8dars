# Generated by Django 5.0.6 on 2024-07-08 09:07

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Klass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Travel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aviakompaniya', models.CharField(max_length=100)),
                ('davomiyligi', models.IntegerField()),
                ('ovqatlanish', models.CharField(max_length=100)),
                ('viza', models.BooleanField()),
                ('price', models.IntegerField()),
                ('bonuslar', models.TextField()),
                ('Klass', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogapp.klass')),
            ],
        ),
    ]