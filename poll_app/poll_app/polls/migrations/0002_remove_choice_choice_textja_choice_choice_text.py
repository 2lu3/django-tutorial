# Generated by Django 4.1.6 on 2023-02-02 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choice',
            name='choice_textjA',
        ),
        migrations.AddField(
            model_name='choice',
            name='choice_text',
            field=models.CharField(default='', max_length=200),
        ),
    ]