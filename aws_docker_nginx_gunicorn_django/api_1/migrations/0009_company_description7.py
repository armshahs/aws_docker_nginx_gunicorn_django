# Generated by Django 5.0.4 on 2024-06-27 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_1', '0008_company_description6'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='description7',
            field=models.TextField(blank=True, null=True),
        ),
    ]
