# Generated by Django 3.0.7 on 2020-07-03 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_remove_event_occurrences'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='archived',
            field=models.BooleanField(default=False, verbose_name='Arquivado'),
        ),
    ]
