# Generated by Django 5.0.6 on 2024-07-04 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PetApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='id_category',
            field=models.CharField(default='sin_categoria', max_length=50),
        ),
        migrations.AddField(
            model_name='producto',
            name='imagen',
            field=models.URLField(default='https://example.com/default_image.jpg'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='precio',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]
