# Generated by Django 3.2.4 on 2021-06-14 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp1', '0005_remove_userdb_dob'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdb',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pic'),
        ),
    ]