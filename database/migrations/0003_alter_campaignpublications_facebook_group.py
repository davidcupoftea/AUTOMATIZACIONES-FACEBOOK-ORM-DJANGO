# Generated by Django 4.1.7 on 2023-04-03 21:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0002_alter_facebookgroup_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaignpublications',
            name='facebook_group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.facebookgroup'),
        ),
    ]
