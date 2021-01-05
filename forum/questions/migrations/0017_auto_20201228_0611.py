# Generated by Django 3.1.4 on 2020-12-28 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0016_auto_20201227_2151'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='dislikes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='question',
            name='likes',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=30, verbose_name='برچسب'),
        ),
    ]
