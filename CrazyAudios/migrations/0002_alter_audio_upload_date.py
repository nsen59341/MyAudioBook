# Generated by Django 5.0.2 on 2024-03-10 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CrazyAudios', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audio',
            name='upload_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
