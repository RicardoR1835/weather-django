# Generated by Django 3.2.13 on 2022-06-28 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='name',
            field=models.CharField(max_length=255, null=True),
        ),
    ]