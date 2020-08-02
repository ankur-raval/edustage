# Generated by Django 3.0.7 on 2020-07-30 19:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admin_app', '0004_user_registration_designation'),
    ]

    operations = [
        migrations.CreateModel(
            name='courses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(default=None, max_length=50, null=True)),
                ('course_fees', models.CharField(default=None, max_length=50, null=True)),
                ('course_detail', models.CharField(default=None, max_length=200, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='user_registration',
            name='class_name',
        ),
        migrations.RemoveField(
            model_name='user_registration',
            name='subject_name',
        ),
        migrations.DeleteModel(
            name='classes',
        ),
        migrations.DeleteModel(
            name='subjects',
        ),
        migrations.AddField(
            model_name='user_registration',
            name='course_name',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='admin_app.courses'),
        ),
    ]
