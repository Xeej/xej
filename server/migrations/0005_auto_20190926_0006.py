# Generated by Django 2.2.5 on 2019-09-26 00:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0004_auto_20190925_2356'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='packet',
            name='gps',
        ),
        migrations.AddField(
            model_name='gps',
            name='packet',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='server.packet'),
            preserve_default=False,
        ),
    ]