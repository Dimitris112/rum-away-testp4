# Generated by Django 5.1.1 on 2024-09-20 15:32

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testimonials', '0006_alter_testimonial_updated_at'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('testimonial', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='testimonials.testimonial')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='testimonial_comments', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
