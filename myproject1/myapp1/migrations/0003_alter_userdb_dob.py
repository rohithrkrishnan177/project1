# Generated by Django 3.2.4 on 2021-06-11 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp1', '0002_auto_20210610_1744'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdb',
            name='dob',
            field=models.DateField(blank=True, max_length=20, null=True),
        ),
    ]
