# Generated by Django 4.2.9 on 2024-01-31 07:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('specialists', '0005_specialist_description_specialist_pricing'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='phone_number',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('payment_method', models.CharField(max_length=50)),
                ('transaction_id', models.CharField(max_length=100)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('phone_number', models.CharField(max_length=15)),
                ('payment_status', models.CharField(choices=[('completed', 'completed'), ('pending', 'pending')], default='pending', max_length=10)),
                ('booking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payments', to='specialists.appointment')),
            ],
        ),
    ]