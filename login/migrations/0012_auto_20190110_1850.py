# Generated by Django 2.1.5 on 2019-01-10 11:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0011_auto_20190110_1845'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loginuser',
            name='favorite',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='favorite.Favorite'),
        ),
    ]
