# Generated by Django 3.2.8 on 2021-10-25 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productocomprado',
            name='idOriginalProduct',
            field=models.IntegerField(),
        ),
    ]