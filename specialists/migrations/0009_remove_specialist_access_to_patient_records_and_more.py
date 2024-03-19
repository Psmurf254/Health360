# Generated by Django 4.2.9 on 2024-03-12 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('specialists', '0008_specialist_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='specialist',
            name='access_to_patient_records',
        ),
        migrations.RemoveField(
            model_name='specialist',
            name='account_security_settings',
        ),
        migrations.RemoveField(
            model_name='specialist',
            name='appointment_reminders',
        ),
        migrations.RemoveField(
            model_name='specialist',
            name='communication_alerts',
        ),
        migrations.RemoveField(
            model_name='specialist',
            name='data_privacy_info',
        ),
        migrations.RemoveField(
            model_name='specialist',
            name='data_privacy_training',
        ),
        migrations.RemoveField(
            model_name='specialist',
            name='multilingual_support_preferences',
        ),
        migrations.RemoveField(
            model_name='specialist',
            name='notification_preferences',
        ),
        migrations.RemoveField(
            model_name='specialist',
            name='patient_interaction_history',
        ),
        migrations.RemoveField(
            model_name='specialist',
            name='patient_ratings',
        ),
        migrations.RemoveField(
            model_name='specialist',
            name='telemedicine_schedule',
        ),
        migrations.AddField(
            model_name='specialist',
            name='Achievements',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='specialist',
            name='Bankground',
            field=models.TextField(blank=True, null=True),
        ),
    ]