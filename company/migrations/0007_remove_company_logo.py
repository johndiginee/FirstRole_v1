# Generated by Django 4.2 on 2023-05-05 18:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0006_company_logo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='logo',
        ),
    ]