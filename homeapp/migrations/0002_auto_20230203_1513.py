# Generated by Django 3.2 on 2023-02-03 09:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homeapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='phonenumber',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='product_name',
        ),
    ]