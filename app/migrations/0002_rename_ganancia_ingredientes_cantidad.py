# Generated by Django 5.0.4 on 2024-05-19 22:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ingredientes',
            old_name='ganancia',
            new_name='cantidad',
        ),
    ]
