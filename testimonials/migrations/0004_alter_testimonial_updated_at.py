# Generated by Django 5.1.1 on 2024-09-15 18:37

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testimonials', '0003_testimonial_created_at_testimonial_updated_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimonial',
            name='updated_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
