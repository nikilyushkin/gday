# Generated by Django 4.0.4 on 2022-06-26 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0010_boardfeed_filters'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boardfeed',
            name='conditions',
            field=models.JSONField(null=True),
        ),
        migrations.AlterField(
            model_name='boardfeed',
            name='filters',
            field=models.JSONField(null=True),
        ),
        migrations.AlterField(
            model_name='boardfeed',
            name='mix',
            field=models.JSONField(null=True),
        ),
    ]
