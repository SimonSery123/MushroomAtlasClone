# Generated by Django 5.0.6 on 2024-06-24 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viewer', '0003_tip_image_tip_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Habitat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterModelOptions(
            name='family',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='mushroom',
            options={'ordering': ['name_cz']},
        ),
        migrations.AlterModelOptions(
            name='recipe',
            options={'ordering': ['title']},
        ),
        migrations.AlterModelOptions(
            name='tip',
            options={'ordering': ['title']},
        ),
        migrations.RemoveField(
            model_name='mushroom',
            name='habitat',
        ),
        migrations.AlterField(
            model_name='tip',
            name='title',
            field=models.CharField(max_length=500),
        ),
        migrations.AddField(
            model_name='mushroom',
            name='habitats',
            field=models.ManyToManyField(related_name='mushrooms', to='viewer.habitat'),
        ),
    ]
