# Generated by Django 3.1.4 on 2021-01-07 17:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0003_socialsetting'),
    ]

    operations = [
        migrations.RenameField(
            model_name='socialsetting',
            old_name='name',
            new_name='icon',
        ),
    ]
