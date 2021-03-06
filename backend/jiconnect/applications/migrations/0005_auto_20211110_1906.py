# Generated by Django 3.2.8 on 2021-11-10 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0004_auto_20211109_1927'),
    ]

    operations = [
        migrations.RenameField(
            model_name='application',
            old_name='status',
            new_name='plan',
        ),
        migrations.AddField(
            model_name='application',
            name='app_type',
            field=models.CharField(blank=True, choices=[('NEW', 'NEW'), ('TEMPORARY', 'TEMPORARY'), ('ROUTING', 'ROUTING'), ('ADDITIONAL LOAD', 'ADDITIONAL LOAD'), ('GROUP APPLICATION', 'GROUP APPLICATION'), ('METER SEPERATION', 'METER SEPERATION')], max_length=200, null=True),
        ),
    ]
