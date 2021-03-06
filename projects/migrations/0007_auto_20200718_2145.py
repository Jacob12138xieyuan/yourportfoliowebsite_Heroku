# Generated by Django 3.0.8 on 2020-07-18 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_auto_20200718_2144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='detail',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='project',
            name='github_link',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='project',
            name='name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='project',
            name='summary',
            field=models.TextField(),
        ),
    ]
