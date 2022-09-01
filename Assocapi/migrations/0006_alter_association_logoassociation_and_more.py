# Generated by Django 4.1 on 2022-08-20 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Assocapi', '0005_association_is_association_accepted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='association',
            name='logoassociation',
            field=models.ImageField(blank=True, null=True, upload_to='images/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='logoorganisation',
            field=models.ImageField(blank=True, null=True, upload_to='images/%Y/%m/%d'),
        ),
    ]