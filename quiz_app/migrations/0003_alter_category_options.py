# Generated by Django 4.1 on 2023-02-19 05:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz_app', '0002_alter_question_asking'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
    ]