# Generated by Django 4.0.4 on 2022-06-04 07:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('animal', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='healthreport',
            name='animal',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='healthreports', to='animal.animal'),
        ),
    ]
