import os
from tools_functions import *

# path_source_html = "D:/COURS LYON 2/COURS M2/TD Gouvernence des données massives/TD_DATALAKE/DATALAKE/0_SOURCE_WEB/" 
# path_landing_zone = "D:/COURS LYON 2/COURS M2/TD Gouvernence des données massives/TD_DATALAKE/DATALAKE/1_LANDING_ZONE/"
# path_curated_zone = "D:/COURS LYON 2/COURS M2/TD Gouvernence des données massives/TD_DATALAKE/DATALAKE/2_CURATED_ZONE/"

path_source_html = "D:/TD_DATALAKE/DATALAKE/0_SOURCE_WEB/"
path_landing_zone = "D:/TD_DATALAKE/DATALAKE/1_LANDING_ZONE/"
path_curated_zone = "D:/TD_DATALAKE/DATALAKE/2_CURATED_ZONE/"

## Landing ZONE
# deplacement dans landing_zone
deplacement_fichier(path_source_html, path_landing_zone)

# création de la métadonnées techniques
creation_metadata_technique(path_source_html,path_landing_zone)

## Curated ZONE
# deplacement dans curate_zone
deplacement_fichier(path_source_html, path_curated_zone,"curated_zone")

# Création des métadonnées descriptif
creation_metadata_descriptif(path_landing_zone,path_curated_zone)

