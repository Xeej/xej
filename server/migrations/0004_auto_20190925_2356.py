# Generated by Django 2.2.5 on 2019-09-25 23:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0003_gps_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gps',
            name='packet',
        ),
        migrations.AddField(
            model_name='packet',
            name='gps',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='server.gps'),
            preserve_default=False,
        ),
    ]