# Generated by Django 5.0.6 on 2024-07-04 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new_app', '0010_alter_customerpayment_card_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerpayment',
            name='expiry_date',
            field=models.CharField(max_length=5),
        ),
    ]
