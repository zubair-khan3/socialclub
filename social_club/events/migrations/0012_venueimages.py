# Generated by Django 4.2.6 on 2023-11-14 12:12

from django.db import migrations, models
import django.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0011_alter_venue_venue_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='VenueImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('venue_images', models.ImageField(blank=True, null=True, upload_to='media/venue')),
                ('venue_pointer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.fields.CharField, to='events.venue')),
            ],
        ),
    ]
