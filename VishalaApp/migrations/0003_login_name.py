# Generated by Django 5.0.4 on 2024-05-01 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VishalaApp', '0002_service_fees'),
    ]

    operations = [
        migrations.AddField(
            model_name='login',
            name='name',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
