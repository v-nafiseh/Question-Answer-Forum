# Generated by Django 3.1.4 on 2021-01-04 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='defalt.jpg', upload_to='prfile_pics'),
        ),
    ]
