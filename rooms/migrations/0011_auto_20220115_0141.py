# Generated by Django 2.2.5 on 2022-01-14 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0010_auto_20220114_2106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='file',
            field=models.ImageField(upload_to='room_photos'),
        ),
    ]
