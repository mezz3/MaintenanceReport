# Generated by Django 2.2 on 2019-05-05 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(default='images/test2.png', null=True, upload_to='images/'),
        ),
    ]
