# Generated by Django 3.1.3 on 2020-12-28 17:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='title',
            new_name='العنوان',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='content',
            new_name='المحتوى',
        ),
    ]