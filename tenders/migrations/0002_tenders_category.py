# Generated by Django 2.2.7 on 2020-02-04 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tenders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tenders',
            name='category',
            field=models.CharField(default='tech', max_length=200),
        ),
    ]