# Generated by Django 4.2.6 on 2023-11-15 11:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0012_venueimages'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venueimages',
            name='venue_pointer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='events.venue'),
        ),
    ]