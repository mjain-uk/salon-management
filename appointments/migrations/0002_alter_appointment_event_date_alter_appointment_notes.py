# Generated by Django 4.2.16 on 2024-09-19 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='event_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='notes',
            field=models.TextField(blank=True),
        ),
    ]