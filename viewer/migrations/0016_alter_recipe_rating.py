# Generated by Django 5.0.6 on 2024-07-11 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viewer', '0015_commentrecipe'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='rating',
            field=models.DecimalField(decimal_places=1, default=0.0, max_digits=2),
        ),
    ]
