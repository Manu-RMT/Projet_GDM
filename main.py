import os
from tools_functions import *

path_source_html = "D:/COURS LYON 2/COURS M2/TD Gouvernence des données massives/TD_DATALAKE/DATALAKE/0_SOURCE_WEB/" 
path_landing_zone = "D:/COURS LYON 2/COURS M2/TD Gouvernence des données massives/TD_DATALAKE/DATALAKE/1_LANDING_ZONE/"

# deplacement dans landing_zone
deplacement_fichier(path_source_html, path_landing_zone)

# deplacement dans curate_zone
deplacement_fichier(path_source_html, path_landing_zone,"curated_zone")

# création de la métadonnées techniques
creation_metadata_technique(path_source_html,path_landing_zone)  




### Création des métadonnées techniques
metadata = []
metadata.append(["Doc_ID","Field","Value"])

path_source = "C:/Etudes/M2/S1/Gestion_de_donnees_massives/Projet/TD_DATALAKE/DATALAKE/1_LANDING_ZONE/GLASSDOOR/SOC/"
metadata.extend(metadata_creation(path_source,"INFO-SOC"))
path_source = "C:/Etudes/M2/S1/Gestion_de_donnees_massives/Projet/TD_DATALAKE/DATALAKE/1_LANDING_ZONE/GLASSDOOR/AVI/"
metadata.extend(metadata_creation(path_source,"AVIS-SOC"))
path_source = "C:/Etudes/M2/S1/Gestion_de_donnees_massives/Projet/TD_DATALAKE/DATALAKE/1_LANDING_ZONE/LINKEDIN/EMP/"
metadata.extend(metadata_creation(path_source,"INFO-EMP"))


### Stockage des métadonnées dans un csv
csv_maker(metadata, "C:/Etudes/M2/S1/Gestion_de_donnees_massives/Projet/TD_DATALAKE/DATALAKE/2_CURATED_ZONE")

# parcours du la métadonnées
