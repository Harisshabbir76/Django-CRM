# Generated by Django 5.1.3 on 2025-01-03 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='age',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='register',
            name='salary',
            field=models.CharField(max_length=100),
        ),
    ]