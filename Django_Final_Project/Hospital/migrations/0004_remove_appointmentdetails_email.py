# Generated by Django 4.1.6 on 2023-02-21 11:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Hospital', '0003_alter_appointmentdetails_email_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointmentdetails',
            name='email',
        ),
    ]
