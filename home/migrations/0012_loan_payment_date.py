# Generated by Django 5.1 on 2024-10-05 00:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_alter_subscriptions_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='loan',
            name='payment_date',
            field=models.DateField(auto_created=True, default=datetime.datetime(2024, 10, 5, 5, 59, 28, 788583)),
            preserve_default=False,
        ),
    ]
