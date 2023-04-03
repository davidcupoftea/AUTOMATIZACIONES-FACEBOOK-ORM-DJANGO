from django.db import models

class OfferType(models.Model):
    type_of_offer_string = models.CharField(max_length=255)

class FacebookGroup(models.Model):
    group = models.CharField(max_length=1000, unique=True)
    offer = models.ManyToManyField(OfferType)

class Campaign(models.Model):
    campaign_name = models.CharField(max_length=1000)
    campaign_type = models.ForeignKey(OfferType, on_delete=models.PROTECT, blank=False, null=False)

class CampaignPublications(models.Model):
    campaign = models.ForeignKey(Campaign, on_delete=models.PROTECT, blank=False, null=False)
    facebook_group = models.ForeignKey(FacebookGroup, on_delete=models.CASCADE, blank=False, null=False)
    sent = models.BooleanField(default=False)