# Generated by Django 5.0.1 on 2024-01-15 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('gender', models.CharField(max_length=10)),
                ('date_of_birth', models.DateField()),
                ('contact_phone', models.CharField(max_length=15)),
                ('contact_email', models.EmailField(max_length=254)),
                ('medical_history', models.TextField()),
                ('allergies', models.TextField()),
                ('medications', models.TextField()),
                ('immunization_records', models.TextField()),
                ('emergency_contact_name', models.CharField(max_length=255)),
                ('emergency_contact_phone', models.CharField(max_length=15)),
                ('telemedicine_consultations_allowed', models.BooleanField(default=True)),
                ('secure_messaging_enabled', models.BooleanField(default=True)),
                ('blood_pressure', models.CharField(blank=True, max_length=20, null=True)),
                ('heart_rate', models.CharField(blank=True, max_length=20, null=True)),
                ('weight', models.CharField(blank=True, max_length=20, null=True)),
                ('current_medications', models.TextField()),
                ('prescription_history', models.TextField()),
                ('preferred_language', models.CharField(max_length=50)),
                ('feedback_ratings', models.FloatField(default=0.0)),
                ('doctor_feedback_history', models.TextField()),
                ('access_to_education_materials', models.BooleanField(default=True)),
                ('appointment_reminders_enabled', models.BooleanField(default=True)),
                ('communication_alerts_enabled', models.BooleanField(default=True)),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='patient_profile_pics/')),
                ('accessibility_tools_enabled', models.BooleanField(default=True)),
                ('notification_preferences', models.BooleanField(default=True)),
                ('account_security_settings', models.BooleanField(default=True)),
            ],
        ),
    ]
