# Generated by Django 4.2.2 on 2023-06-22 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_contributor_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='contributor',
            name='email_from_patch',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]