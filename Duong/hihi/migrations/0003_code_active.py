# Generated by Django 2.1.1 on 2018-10-07 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hihi', '0002_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='code',
            name='active',
            field=models.CharField(default=0, max_length=2),
            preserve_default=False,
        ),
    ]
