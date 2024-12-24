# Generated by Django 5.1.2 on 2024-11-17 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cc', '0031_alter_feedback_options_remove_feedback_comp_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='complaint',
            name='resolved_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='feedback',
            name='rating',
            field=models.PositiveSmallIntegerField(default=5),
        ),
    ]