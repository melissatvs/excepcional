# Generated by Django 3.0.7 on 2020-07-03 18:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_event_occurrences'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='occurrences',
        ),
    ]
