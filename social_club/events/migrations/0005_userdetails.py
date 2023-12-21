# Generated by Django 4.2.6 on 2023-11-08 08:46

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('events', '0004_alter_events_attendees'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_city', models.CharField(blank=True, max_length=50, null=True)),
                ('user_state', models.CharField(blank=True, max_length=50, null=True)),
                ('user_country', models.CharField(blank=True, default='Not Defined', max_length=100, null=True)),
                ('user_number', models.CharField(max_length=20, validators=[django.core.validators.RegexValidator(regex='^(\\+?\\d{1,3})?[-.\\s]?\\(?\\d{3}\\)?[-.\\s]?\\d{3}[-.\\s]?\\d{4}$')])),
                ('user_picture', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('user_info', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]