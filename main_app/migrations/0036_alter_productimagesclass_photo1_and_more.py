# Generated by Django 5.1 on 2024-11-24 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0035_alter_staticphotoclass_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimagesclass',
            name='photo1',
            field=models.ImageField(upload_to='images/products'),
        ),
        migrations.AlterField(
            model_name='productimagesclass',
            name='photo2',
            field=models.ImageField(upload_to='images/products'),
        ),
        migrations.AlterField(
            model_name='productimagesclass',
            name='photo3',
            field=models.ImageField(upload_to='images/products'),
        ),
        migrations.AlterField(
            model_name='productimagesclass',
            name='photo4',
            field=models.ImageField(upload_to='images/products'),
        ),
        migrations.AlterField(
            model_name='productimagesclass',
            name='photo5',
            field=models.ImageField(blank=True, upload_to='images/products'),
        ),
        migrations.AlterField(
            model_name='productimagesclass',
            name='photo6',
            field=models.ImageField(blank=True, upload_to='images/products'),
        ),
        migrations.AlterField(
            model_name='productimagesclass',
            name='photo7',
            field=models.ImageField(blank=True, upload_to='images/products'),
        ),
        migrations.AlterField(
            model_name='productimagesclass',
            name='photo8',
            field=models.ImageField(blank=True, upload_to='images/products'),
        ),
        migrations.AlterField(
            model_name='productimagesclass',
            name='photoZ1',
            field=models.ImageField(blank=True, upload_to='images/products/zoom'),
        ),
        migrations.AlterField(
            model_name='productimagesclass',
            name='photoZ2',
            field=models.ImageField(blank=True, upload_to='images/products/zoom'),
        ),
        migrations.AlterField(
            model_name='productimagesclass',
            name='photoZ3',
            field=models.ImageField(blank=True, upload_to='images/products/zoom'),
        ),
        migrations.AlterField(
            model_name='productimagesclass',
            name='photoZ4',
            field=models.ImageField(blank=True, upload_to='images/products/zoom'),
        ),
        migrations.AlterField(
            model_name='productimagesclass',
            name='photoZ5',
            field=models.ImageField(blank=True, upload_to='images/products/zoom'),
        ),
        migrations.AlterField(
            model_name='productimagesclass',
            name='photoZ6',
            field=models.ImageField(blank=True, upload_to='images/products/zoom'),
        ),
        migrations.AlterField(
            model_name='productimagesclass',
            name='photoZ7',
            field=models.ImageField(blank=True, upload_to='images/products/zoom'),
        ),
        migrations.AlterField(
            model_name='productimagesclass',
            name='photoZ8',
            field=models.ImageField(blank=True, upload_to='images/products/zoom'),
        ),
    ]
