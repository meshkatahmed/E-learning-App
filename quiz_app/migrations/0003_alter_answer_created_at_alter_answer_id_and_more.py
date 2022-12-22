# Generated by Django 4.1 on 2022-12-22 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz_app', '0002_remove_answer_basemodel_ptr_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='created_at',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='answer',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='category',
            name='created_at',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='question',
            name='created_at',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
