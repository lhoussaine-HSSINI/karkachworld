# Generated by Django 4.1 on 2022-08-18 18:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Assocapi', '0003_association_is_accepted'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='association',
            name='is_accepted',
        ),
    ]