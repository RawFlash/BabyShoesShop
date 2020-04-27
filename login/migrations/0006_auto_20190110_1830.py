# Generated by Django 2.1.5 on 2019-01-10 11:30

import builtins
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0005_auto_20190110_1829'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loginuser',
            name='favorite',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='favorite.Favorite'),
        ),
        migrations.AlterField(
            model_name='loginuser',
            name='login',
            field=models.CharField(blank=True, default=builtins.id, max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='loginuser',
            name='password',
            field=models.CharField(blank=True, default=builtins.id, max_length=64, null=True),
        ),
    ]
