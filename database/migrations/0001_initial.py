# Generated by Django 4.1.7 on 2023-03-29 08:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Campaign',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('campaign_name', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='OfferType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_of_offer_string', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='FacebookGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.CharField(max_length=1000)),
                ('offer', models.ManyToManyField(to='database.offertype')),
            ],
        ),
        migrations.CreateModel(
            name='CampaignPublications',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sent', models.BooleanField(default=False)),
                ('campaign', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='database.campaign')),
                ('facebook_group', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='database.facebookgroup')),
            ],
        ),
        migrations.AddField(
            model_name='campaign',
            name='campaign_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='database.offertype'),
        ),
    ]
