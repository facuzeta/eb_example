# Generated by Django 3.1.3 on 2020-11-12 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unica_app', '0003_auto_20201112_1441'),
    ]

    operations = [
        migrations.AlterField(
            model_name='numerohistorico',
            name='ip',
            field=models.TextField(blank=True),
        ),
    ]