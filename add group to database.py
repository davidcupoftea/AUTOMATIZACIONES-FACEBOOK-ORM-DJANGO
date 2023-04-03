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

# conn = sqlite3.connect('C:\\Users\\Santi\\Desktop\\DAVID-2\\AUTOMATIZACIONES FACEBOOK\\src\\facebook spamming.sqlite3');
# c = conn.cursor()

#videoeditor
#asistentevirtual
#copywriter
#diseñador
#dataentry
#programador
#traductor

group = 'https://www.facebook.com/groups/616604882961361'
list_of_offers = ['programador']

def add_group_to_database(group, list_of_offers):
    group_to_save = FacebookGroup(group=group)
    group_to_save.save()
    for offer in list_of_offers:
        offer_type = OfferType.objects.get(type_of_offer_string=offer)
        group_to_save.offer.add(offer_type)
    # c.execute("INSERT INTO GRUPOS_FACEBOOK (URL) VALUES ('" + group +"')")
    # id_of_group = c.execute("SELECT ROWID FROM GRUPOS_FACEBOOK WHERE URL='" + group +"'")
    # id_of_group = id_of_group.fetchone()
    # id_of_group = id_of_group[0]
    # for offer in list_of_offers:
    #     res = c.execute("SELECT OFFER_ID FROM OFFER WHERE OFFER_NAME ='" + offer + "'")
    #     result = res.fetchone()
    #     #print(result)
    #     for re in result:
    #         c.execute("INSERT INTO OFFER_GROUP (OFFER_ID, GROUP_ID) VALUES ('" + str(re) + "','" + str(id_of_group) + "')")
    #         #c.execute("INSERT INTO OFFER_GROUP (OFFER_ID, GROUP_ID) VALUES ('1','1')")
    #         conn.commit()
    #         #print(re)

add_group_to_database(group, list_of_offers)
