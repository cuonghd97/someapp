# Generated by Django 2.1.1 on 2018-09-28 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manageuser', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='typeuser',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
