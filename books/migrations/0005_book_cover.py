# Generated by Django 5.0.4 on 2024-04-23 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_review_book'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='cover',
            field=models.ImageField(blank=True, upload_to='cover/'),
        ),
    ]
