# Generated by Django 5.1.1 on 2024-09-21 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testimonials', '0009_alter_comment_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='was_edited',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='testimonial',
            name='was_edited',
            field=models.BooleanField(default=False),
        ),
    ]
