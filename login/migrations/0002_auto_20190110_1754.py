# Generated by Django 2.1.5 on 2019-01-10 10:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='loginuser',
            old_name='name',
            new_name='login',
        ),
    ]
