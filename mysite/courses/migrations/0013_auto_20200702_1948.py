# Generated by Django 3.0.7 on 2020-07-02 19:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0012_auto_20200702_1931'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='majors',
            new_name='major',
        ),
    ]
