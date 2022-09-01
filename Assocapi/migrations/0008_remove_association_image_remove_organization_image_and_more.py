# Generated by Django 4.1 on 2022-09-01 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Assocapi', '0007_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='association',
            name='image',
        ),
        migrations.RemoveField(
            model_name='organization',
            name='image',
        ),
        migrations.AddField(
            model_name='organization',
            name='is_organisation_accepted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='post',
            name='is_post_accepted',
            field=models.BooleanField(default=False),
        ),
    ]
