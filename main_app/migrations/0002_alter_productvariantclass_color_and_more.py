# Generated by Django 5.1 on 2025-01-01 12:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productvariantclass',
            name='color',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='colors', to='main_app.colorclass'),
        ),
        migrations.AlterField(
            model_name='productvariantclass',
            name='size',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='sizes', to='main_app.sizeclass'),
        ),
    ]
