# Generated by Django 4.2 on 2023-05-05 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0005_remove_company_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='logo',
            field=models.ImageField(default='logo.jpg', upload_to='company_logo'),
        ),
    ]