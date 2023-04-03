import sqlite3
# main.py
# Django specific settings
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

### Have to do this for it to work in 1.9.x!
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
#############


# Your application specific imports
from database.models import *


def change_campaign_publication_to_sent():
    campaign = CampaignPublications.objects.get(pk=1)
    campaign.sent = True
    campaign.save()

change_campaign_publication_to_sent()