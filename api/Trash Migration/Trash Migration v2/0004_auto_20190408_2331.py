# Generated by Django 2.2 on 2019-04-08 16:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_postactivity_members'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postactivity',
            name='members',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Member'),
        ),
    ]
