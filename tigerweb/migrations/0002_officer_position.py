# Generated by Django 2.2.4 on 2019-08-29 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tigerweb', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='officer',
            name='position',
            field=models.CharField(default='Treasurer', max_length=128),
            preserve_default=False,
        ),
    ]
