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

# import sqlite3
# conn = sqlite3.connect('C:\\Users\\Santi\\Desktop\\DAVID-2\\AUTOMATIZACIONES FACEBOOK\\facebook spamming.sqlite3');
# c = conn.cursor()


#videoeditor
#asistentevirtual
#copywriter
#diseñador
#dataentry
#programador
#traductor

def add_campaign_and_publications(tipo, nombre_campaña):
    offer_type = OfferType.objects.get(type_of_offer_string=tipo)
    campaign_object = Campaign(campaign_name=nombre_campaña, campaign_type=offer_type)
    campaign_object.save()

    offer = OfferType.objects.get(type_of_offer_string=tipo)

    groups = offer.facebookgroup_set.all()
    #print(groups)
    for group in groups:
        campaign_to_save = CampaignPublications(campaign=campaign_object,facebook_group=group)
        campaign_to_save.save()

    # c.execute("INSERT INTO CAMPAÑAS (NOMBRE_CAMPAÑA, TIPO_CAMPAÑA) VALUES('" + nombre_campaña + "','" + tipo + "')")
    # conn.commit()
    # resp = c.execute("SELECT MAX(rowid) FROM CAMPAÑAS LIMIT 1;")
    # res = resp.fetchone()
    # re = res[0]
    # print(re)
    # url = 1
    # offer_id = c.execute("SELECT OFFER_ID FROM OFFER WHERE OFFER_NAME='" + tipo +"'")
    # offer_id = offer_id.fetchone()
    # offer_id = offer_id[0]
    # #print('offer_id', offer_id)
    # groups_id = c.execute("SELECT GROUP_ID FROM OFFER_GROUP WHERE OFFER_ID='" + str(offer_id) +"'")
    # groups_id = groups_id.fetchall()
    # print('groups_id', groups_id)
    # #groups_id_tuple = []
    # # for group_id in groups_id:
    # #     print(group_id)
    # #     for group in group_id:
    # #         groups_id_tuple.append(group)
    # groups_id_tuple = [item for t in groups_id for item in t]
    # print(tuple(groups_id_tuple))
    # urls = c.execute("SELECT URL FROM GRUPOS_FACEBOOK WHERE ROWID IN " + str(tuple(groups_id_tuple)) + "")
    # urls = urls.fetchall()
    # print('urls', urls)
    # urls_tuple = [item for t in urls for item in t]
    # for url in urls_tuple:
    #     c.execute("INSERT INTO PUBLICACIONES_CAMPAÑAS (CAMPAÑA_ID, GROUP_ID, ENVIADO) VALUES('" + str(re) + "','" + str(url) + "','0')")
    # conn.commit()

add_campaign_and_publications('programador', 'Campaña 1')