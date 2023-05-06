# Generated by Django 4.2 on 2023-05-05 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0003_company_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='image',
        ),
        migrations.AddField(
            model_name='company',
            name='logo',
            field=models.ImageField(default='logo.jpg', upload_to='company_logo'),
        ),
    ]