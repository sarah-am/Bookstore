# Generated by Django 2.1.7 on 2019-02-13 16:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_auto_20190213_1618'),
    ]

    operations = [
        migrations.RenameField(
            model_name='seller',
            old_name='seller',
            new_name='salesman',
        ),
    ]
