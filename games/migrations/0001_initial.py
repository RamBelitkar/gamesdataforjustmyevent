# Generated by Django 5.1.2 on 2024-12-25 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MuscialDescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('musical_name', models.CharField(max_length=255)),
                ('musical_description', models.TextField()),
            ],
        ),
    ]
