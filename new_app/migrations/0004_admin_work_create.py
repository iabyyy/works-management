# Generated by Django 5.0.6 on 2024-06-29 05:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new_app', '0003_alter_booking_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin_Work_Create',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('two wheeler with gear', 'two wheeler with gear'), ('two wheeler without gear', 'two wheeler without gear'), ('three wheeler', 'three wheeler'), ('four wheeler', 'four wheeler')], max_length=50)),
                ('vehicle_no', models.PositiveIntegerField(null=True)),
                ('vehicle_name', models.CharField(blank=True, max_length=100, null=True)),
                ('vehicle_model', models.CharField(blank=True, max_length=100, null=True)),
                ('vehicle_brand', models.CharField(blank=True, max_length=100, null=True)),
                ('problem_description', models.CharField(blank=True, max_length=100, null=True)),
                ('date', models.DateField(auto_now=True)),
                ('cost', models.PositiveIntegerField(blank=True, null=True)),
                ('status', models.CharField(choices=[('repairing', 'repairing'), ('repairing done', 'repairing done'), ('released', 'released')], default='Pending', max_length=100, null=True)),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='new_app.customer')),
                ('worksmanager', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='new_app.worksmanager')),
            ],
        ),
    ]
