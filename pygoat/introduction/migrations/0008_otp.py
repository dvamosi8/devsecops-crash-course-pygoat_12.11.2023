# Generated by Django 3.0.6 on 2021-04-24 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('introduction', '0007_auto_20210418_0022'),
    ]

    operations = [
        migrations.CreateModel(
            name='otp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=200)),
                ('otp', models.IntegerField(max_length=300)),
            ],
        ),
    ]