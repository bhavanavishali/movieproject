# Generated by Django 4.2.7 on 2023-12-01 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movies',
            name='image',
            field=models.ImageField(default='aaa', upload_to=''),
            preserve_default=False,
        ),
    ]
