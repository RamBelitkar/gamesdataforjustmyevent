# Generated by Django 5.1.2 on 2024-12-25 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='muscialdescription',
            name='musical_image',
            field=models.ImageField(default='images/placeholder.png', upload_to='images/'),
        ),
    ]
