# Generated by Django 4.2.2 on 2023-06-06 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_contributor_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contributor',
            name='company',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
