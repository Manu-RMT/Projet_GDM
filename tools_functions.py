import os,shutil, fnmatch, csv
from datetime import datetime
from tools_getter_setter import *
from bs4 import BeautifulSoup

#==============================================================================
#-- Création du script des déplacement des fichiers
#==============================================================================
def deplacement_fichier(path_source,path_destinatation, zone="landing_zone"):  
    
    #filtre des fichiers
    filtre_link_emp = "*INFO-EMP*.html"
    filter_glassdor_avis_soc = "*AVIS-SOC*.html"
    filter_glassdor_info_soc = "*INFO-SOC*.html"
    
    files = os.listdir(path_source)
    
    for file in files:   
        t = datetime.now()
        dh = str(t.date()) +"-" + str(t.hour) + "-"
        
        # Copie des ficihiers sources dans le bon répertoire
        # LINKEDIN EMP
        if fnmatch.fnmatch(file,filtre_link_emp) == True : 
            dossier_dest = "LINKEDIN/EMP"
            file_source = os.path.join(path_source, file)
            if zone == "landing_zone":
                file_dest = os.path.join(path_destinatation,dossier_dest, dh + file)
            else:
                file_dest = os.path.join(path_destinatation,dossier_dest,file)
            if os.path.exists(file_source):
                shutil.copy(file_source,file_dest)  
            
        # GLASSDOOR AVIS
        if fnmatch.fnmatch(file,filter_glassdor_avis_soc) == True :
           dossier_dest = "GLASSDOOR/AVI"
           file_source = os.path.join(path_source, file)
           if zone == "landing_zone":
               file_dest = os.path.join(path_destinatation,dossier_dest, dh + file)
           else:
               file_dest = os.path.join(path_destinatation,dossier_dest,file)    
           if os.path.exists(file_source):
               shutil.copy(file_source,file_dest)  
            
          # GLASSDOOR SOC
        if fnmatch.fnmatch(file,filter_glassdor_info_soc) == True :
            dossier_dest = "GLASSDOOR/SOC"
            file_source = os.path.join(path_source, file)
            if zone == "landing_zone":
                file_dest = os.path.join(path_destinatation,dossier_dest, dh + file)
            else:
                file_dest = os.path.join(path_destinatation,dossier_dest,file)
            if os.path.exists(file_source):
                shutil.copy(file_source,file_dest)  
            

#==============================================================================
#-- Création du script des métadonnées techniques
#==============================================================================
def creation_metadata_technique(path_source_data,path_landing_zone):
    path_metadata = os.path.join(path_landing_zone,"MetaDonnees", "metadata.csv")
    metadata = open(path_metadata,"w", encoding="utf8")
    
    myListeDeLigneAEcrire = [] 
    #-- Remplissage l'entete de la liste 
    myListeDeLigneAEcrire.append('"cle_unique";"colonne";"valeur"'+"\n")
    
    
    folders = os.listdir(path_landing_zone)
    for folder in folders:
        if folder in ['GLASSDOOR','LINKEDIN']:
            for folder2 in os.listdir(path_landing_zone+folder):
                print(folder2)
                for file in os.listdir(path_landing_zone+folder+"/"+folder2):
                    # cle unique
                    position_dernier_tiret = file.rfind('-')
                    if position_dernier_tiret != -1:
                        cle = file[position_dernier_tiret + 1:]
                        cle = cle[:-5]
                    #source 
                    source_file = folder
                    # date récupération
                    date_file = file[slice(0,10)]
                    #type
                    nom_file = file.split('-')
                    type_file = '-'.join(nom_file[5:7])
                    #lien html
                    lien_file = os.path.join(path_landing_zone,folder,folder2,file)
                    #chemin fichier
                    
                    # construction des métadonnées
                    ligne_date_publi = cle + ";" + "date_heure_recuperation" + ";" + date_file+"\n" 
                    ligne_nom_fichier = cle + ";" + "nom_fichier" + ";" + file + "\n"
                    ligne_prov_fichier_html = cle + ";" + "provenance_du_fichier" + ";" + path_source_data + "\n"
                    ligne_dest_ficiher_html = cle + ";" + "destination_du_fichier" + ";" + os.path.join(path_landing_zone,folder,folder2) + "\n"
                    ligne_source_fichier = cle + ";" + "source_du_fichier" + ";" + source_file + "\n"
                    ligne_type_fichier = cle + ";" + "type_du_fichier" + ";" + type_file + "\n"
                    ligne_lien_fichier = cle + ";" + "lien_fichier" + ";" + lien_file + "\n"
                    ligne_taille_ficiher = cle + ";" + "taille_du_fichier" + ";" + str(len(file)) + "\n" 
                    
                    # Rempliisage des lignes de metadonnes
                    myListeDeLigneAEcrire.append(ligne_date_publi)
                    myListeDeLigneAEcrire.append(ligne_nom_fichier)
                    myListeDeLigneAEcrire.append(ligne_prov_fichier_html)
                    myListeDeLigneAEcrire.append(ligne_dest_ficiher_html)
                    myListeDeLigneAEcrire.append(ligne_source_fichier)
                    myListeDeLigneAEcrire.append(ligne_type_fichier)
                    myListeDeLigneAEcrire.append(ligne_lien_fichier)
                    myListeDeLigneAEcrire.append(ligne_taille_ficiher)
    # Ecriture dans le fichier de métadonnées techniques
    metadata.writelines(myListeDeLigneAEcrire)
    metadata.close()
    

#==============================================================================
#-- Création du script des lignes de métadonnées descriptives
#==============================================================================
def metadata_creation(path_source,type):
    #metadata creation
    metadata = []
    
    files = os.listdir(path_source)
    for file in files:
        #doc preparation
        myHTMLPathFileName = path_source+file
        f = open(myHTMLPathFileName, "r", encoding="utf8")
        myHTMLContents = f.read()
        f.close()

        mySoup = BeautifulSoup(myHTMLContents, 'lxml')
        print(mySoup)
        doc_id = file[-16:-8]
        value = []
        if type == "INFO-SOC":
            field = ["company", "city", "nb_employee", "company_description","type"]
            value.append(Get_nom_entreprise_SOC(mySoup))
            value.append(Get_ville_entreprise_SOC(mySoup))
            value.append(Get_taille_entreprise_SOC(mySoup))
            value.append(Get_description_entreprise_SOC(mySoup))
            value.append("INFO-SOC")
        # elif type == "AVIS-SOC":
        #     field = ["company","avg_rating","type"]
        #     value.append(Get_nom_entreprise_AVI(mySoup))
        #     value.append(Get_note_moy_entreprise_AVI(mySoup))
        #     value.append("AVIS-SOC")
        # else:
        #     field = ["lib_job","company","city", "job_description","type"]
        #     value.append(Get_libelle_emploi_EMP(mySoup))
        #     value.append(Get_nom_entreprise_EMP(mySoup))
        #     value.append(Get_ville_emploi_EMP(mySoup))
        #     value.append(Get_texte_emploi_EMP(mySoup))
        #     value.append("INFO-EMP")
        # for i, column in enumerate(field) :
        #     metadata.append([doc_id,column,value[i]])
            
    return(metadata) 
    
    
def csv_maker(data_list,path):
    
    

    myPathMetaDataOut = path
    myPathFileNameMetaDataOut = myPathMetaDataOut + "/" + "metadata.csv"

    f = open(myPathFileNameMetaDataOut, 'w', newline='', encoding="utf8")

    myWriter = csv.writer(f, delimiter=';', quotechar='"',  quoting=csv.QUOTE_ALL, lineterminator='\n')

    myWriter.writerows(data_list)
    f.close()


    
    
    myPathMetaDataOut = path
    myPathFileNameMetaDataOut = os.path.join(myPathMetaDataOut, "metadata.csv")

    f = open(myPathFileNameMetaDataOut, 'w', newline='', encoding="utf8")

    myWriter = csv.writer(f, delimiter=';', quotechar='"',  quoting=csv.QUOTE_ALL, lineterminator='\n')

    myWriter.writerows(data_list)
    f.close()    
    
    
#==============================================================================
#-- Création du script des métadonnées descriptives
#==============================================================================
def creation_metadata_descriptif(path_landing_zone,path_curated_zone):     
    metadata = []
    metadata.append(["Doc_ID","Field","Value"])
    
    path_source = path_landing_zone + "GLASSDOOR/SOC/"
    metadata.extend(metadata_creation(path_source,"INFO-SOC"))
    path_source = path_landing_zone + "GLASSDOOR/AVI/"
    metadata.extend(metadata_creation(path_source,"AVIS-SOC"))
    path_source =  path_landing_zone + "LINKEDIN/EMP/"
    metadata.extend(metadata_creation(path_source,"INFO-EMP"))
    
    
    ### Stockage des métadonnées dans un csv
    csv_maker(metadata, path_curated_zone)
       