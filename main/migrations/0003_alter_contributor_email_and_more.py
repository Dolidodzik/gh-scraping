# Generated by Django 4.2.2 on 2023-06-06 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_rename_repo_contributor_repos_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contributor',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='contributor',
            name='followers_count',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='contributor',
            name='hireable',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
