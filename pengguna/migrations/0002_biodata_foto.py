# Generated by Django 5.1.6 on 2025-03-15 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pengguna', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='biodata',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='pengguna'),
        ),
    ]
