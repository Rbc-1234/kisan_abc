# Generated by Django 3.2.8 on 2022-03-02 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20220223_1644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contest_category',
            name='masterstatus',
            field=models.CharField(blank=True, default=None, max_length=200, null=True),
        ),
    ]
