# Generated by Django 3.0.3 on 2020-02-05 07:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='imagae',
            new_name='image',
        ),
    ]
