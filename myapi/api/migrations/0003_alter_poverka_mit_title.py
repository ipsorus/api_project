# Generated by Django 3.2.7 on 2021-09-27 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_rename_poverki_poverka'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poverka',
            name='mit_title',
            field=models.CharField(max_length=256),
        ),
    ]
