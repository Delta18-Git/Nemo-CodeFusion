# Generated by Django 5.1 on 2024-10-05 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_subscriptions_payment_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='loan',
            name='last_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
