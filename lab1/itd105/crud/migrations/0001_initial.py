# Generated by Django 5.0 on 2023-12-22 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='medicine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('med_name', models.CharField(max_length=100)),
                ('med_brand', models.CharField(max_length=100)),
                ('med_dosage', models.CharField(max_length=100)),
                ('med_expiry', models.DateField()),
                ('med_stock', models.IntegerField()),
                ('med_status', models.CharField(max_length=100)),
            ],
        ),
    ]
