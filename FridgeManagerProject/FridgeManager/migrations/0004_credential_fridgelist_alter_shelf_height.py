# Generated by Django 4.1.7 on 2023-04-27 12:38

from django.db import migrations, models
import djongo.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('FridgeManager', '0003_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='credential',
            name='fridgeList',
            field=djongo.models.fields.JSONField(default=dict),
        ),
        migrations.AlterField(
            model_name='shelf',
            name='height',
            field=models.FloatField(default=True),
        ),
    ]
