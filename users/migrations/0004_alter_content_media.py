# Generated by Django 5.0.3 on 2024-03-30 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='media',
            field=models.ImageField(blank=True, null=True, upload_to='content/'),
        ),
    ]
