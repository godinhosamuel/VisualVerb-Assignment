# Generated by Django 4.2.6 on 2023-10-14 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mainApp", "0004_supermarketsale_time_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="supermarketsale",
            name="id",
        ),
        migrations.AlterField(
            model_name="supermarketsale",
            name="invoice_id",
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
    ]
