# Generated by Django 5.1 on 2024-11-23 16:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0027_remove_productclass_brand_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='productvariantclass',
            name='brand',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='brands', to='main_app.brandclass'),
        ),
        migrations.AddField(
            model_name='productvariantclass',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='main_app.categoryclass'),
        ),
        migrations.AlterField(
            model_name='productvariantclass',
            name='color',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='colors', to='main_app.colorclass'),
        ),
        migrations.AlterField(
            model_name='productvariantclass',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='main_app.productclass'),
        ),
        migrations.AlterField(
            model_name='productvariantclass',
            name='size',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sizes', to='main_app.sizeclass'),
        ),
    ]
