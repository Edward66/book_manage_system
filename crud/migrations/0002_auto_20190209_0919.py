# Generated by Django 2.1.5 on 2019-02-09 09:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='comment_number',
        ),
        migrations.RemoveField(
            model_name='book',
            name='read_number',
        ),
    ]