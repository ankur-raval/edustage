# Generated by Django 3.0.8 on 2020-07-24 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_app', '0003_auto_20200723_1220'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_registration',
            name='designation',
            field=models.CharField(choices=[('manager', 'manager'), ('principal', 'principal')], default=None, max_length=20, null=True),
        ),
    ]
