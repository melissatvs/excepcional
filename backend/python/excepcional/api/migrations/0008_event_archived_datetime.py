# Generated by Django 3.0.7 on 2020-07-03 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_event_archived'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='archived_datetime',
            field=models.DateTimeField(null=True, verbose_name='Data/Hora Arquivado'),
        ),
    ]
