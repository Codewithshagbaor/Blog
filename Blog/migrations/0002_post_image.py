# Generated by Django 4.1.3 on 2023-01-11 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='', upload_to='Posts'),
            preserve_default=False,
        ),
    ]
