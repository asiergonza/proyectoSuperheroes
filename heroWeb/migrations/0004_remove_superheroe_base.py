# Generated by Django 3.2.8 on 2021-12-10 08:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('heroWeb', '0003_superheroe_base'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='superheroe',
            name='base',
        ),
    ]