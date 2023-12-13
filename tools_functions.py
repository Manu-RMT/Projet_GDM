import os,shutil, fnmatch, csv
from datetime import datetime


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
                    
                    # date récupération
                    date_file = file[slice(0,10)]
                    #type
                    type_file = folder + "_" + folder2
                    #lien html
                    lien_file = os.path.join(path_landing_zone,folder,folder2,file)
                    
                    # construction des métadonnées
                    ligne_date_publi = cle + ";" + "date_heure_recuperation" + ";" + date_file+"\n" 
                    ligne_nom_fichier = cle + ";" + "nom_fichier" + ";" + file + "\n"
                    ligne_prov_fichier_html = cle + ";" + "provenance_du_fichier" + ";" + path_source_data + "\n"
                    ligne_dest_ficiher_html = cle + ";" + "destination_du_fichier" + ";" + os.path.join(path_landing_zone,folder,folder2) + "\n"
                    ligne_taille_ficiher = cle + ";" + "taille_du_fichier" + ";" + str(len(file)) + "\n" 
                    
                    # Rempliisage des lignes de metadonnes
                    myListeDeLigneAEcrire.append(ligne_date_publi)
                    myListeDeLigneAEcrire.append(ligne_nom_fichier)
                    myListeDeLigneAEcrire.append(ligne_prov_fichier_html)
                    myListeDeLigneAEcrire.append(ligne_dest_ficiher_html)
                    myListeDeLigneAEcrire.append(ligne_taille_ficiher)
    # Ecriture dans le fichier de métadonnées techniques
    metadata.writelines(myListeDeLigneAEcrire)
    metadata.close()
    
        

# ==============================================================================
#-- LINKEDIN (EMPLOI) : Libellé de l'offre
#==============================================================================
def Get_libelle_emploi_EMP(Soup):
    myTest = Soup.find_all('h1', attrs = {'class':'topcard__title'}) 
    if (myTest == []) : 
        Result = 'NULL'
    else:
        myTest = str(myTest[0].text)
        if (myTest == []) : 
            Result = 'NULL'
        else:
            Result = myTest
    return(Result)

#print(Get_libelle_emploi_EMP(mySoup))


#==============================================================================
#-- LINKEDIN (EMPLOI) : Nom de la Société demandeuse
#==============================================================================
def Get_nom_entreprise_EMP(Soup):
    myTest = Soup.find_all('span', attrs = {'class':'topcard__flavor'}) 
    if (myTest == []) : 
        Result = 'NULL'
    else:
        myTest = str(myTest[0].text)
        if (myTest == []) : 
            Result = 'NULL'
        else:
            Result = myTest
    return(Result)

#print(Get_nom_entreprise_EMP(mySoup))



#==============================================================================
#-- LINKEDIN (EMPLOI) : Ville de l'emploi proposé
#==============================================================================
def Get_ville_emploi_EMP (Soup):
    myTest = Soup.find_all('span', attrs = {'class':'topcard__flavor topcard__flavor--bullet'}) 
    if (myTest == []) : 
        Result = 'NULL'
    else:
        myTest = str(myTest[0].text)
        if (myTest == []) : 
            Result = 'NULL'
        else:
            Result = myTest
    return(Result)

#print(Get_ville_emploi_EMP(mySoup))


#==============================================================================
#-- LINKEDIN (EMPLOI) : Texte de l'offre d'emploi
#==============================================================================
def Get_texte_emploi_EMP (Soup):
    myTest = Soup.find_all('div', attrs = {"description__text description__text--rich"})
    if (myTest == []) : 
        Result = 'NULL'
    else:
        myTest = str(myTest[0].text)
        if (myTest == []) : 
            Result = 'NULL'
        else:
            Result = myTest
    return(Result)

#==============================================================================
#-- GLASSDOOR (AVIS) : Fonction renvoyant <nom_entreprise>
#==============================================================================
def Get_nom_entreprise_AVI (Soup):
    myTest = Soup.find_all('div', attrs = {"class":"header cell info"})[0].span.contents[0]
    if (myTest == []) : 
        Result = 'NULL'
    else:
        Result = myTest
    return(Result)

#print(Get_nom_entreprise_AVI(mySoup))



#==============================================================================
#-- GLASSDOOR (AVIS) : Fonction renvoyant <Note_moy_entreprise>
#==============================================================================
def Get_note_moy_entreprise_AVI(Soup):
    myTest = Soup.find_all('div', attrs = {'class':'v2__EIReviewsRatingsStylesV2__ratingNum v2__EIReviewsRatingsStylesV2__large'})[0].contents[0]
    if (myTest == []) : 
        Result = 'NULL'
    else:
        Result = myTest  
    return(Result)



#==============================================================================
#-- GLASSDOOR (SOCIETE) : Fonction renvoyant le nom de l'entreprise
#==============================================================================
import re
def Get_nom_entreprise_SOC(Soup):
    myTest = Soup.find_all('h1', attrs = {" strong tightAll"})[0]

    if (myTest == []) : 
        Result = 'NULL'
    else:
        myTxtTmp = str(myTest)
        Result = re.sub(r'(.*)<h1 class=" strong tightAll" data-company="(.*)" title="">(.*)', r'\2', myTxtTmp)
    return(Result)



#==============================================================================
#-- GLASSDOOR (SOCIETE) : Fonction renvoyant la ville de l'entreprise
#==============================================================================

def Get_ville_entreprise_SOC(Soup):
    myTest = str(Soup.find_all('div', attrs = {'class':"infoEntity"})[1].span.contents[0])

    if (myTest == []) : 
        Result = 'NULL'
    else:
        myTxtTmp = str(myTest)
        myTxtTmp1 = re.sub(r'(.*)<h1 class=" strong tightAll" data-company="(.*)" title="">(.*)', r'\2', myTxtTmp)
        Result = myTxtTmp1
    return(Result)


#==============================================================================
#-- GLASSDOOR (SOCIETE) : Fonction renvoyant la taille de l'entreprise
#==============================================================================

def Get_taille_entreprise_SOC(Soup):
    myTest = str(Soup.find_all('div', attrs = {'class':"infoEntity"})[2].span.contents[0])

    if (myTest == []) : 
        Result = 'NULL'
    else:
        myTxtTmp = str(myTest)
        myTxtTmp1 = re.sub(r'(.*)<h1 class=" strong tightAll" data-company="(.*)" title="">(.*)', r'\2', myTxtTmp)
        Result = myTxtTmp1
    return(Result)

#print(Get_taille_entreprise_SOC(mySoup))


#==============================================================================
#-- GLASSDOOR (SOCIETE) : Fonction renvoyant la description de l'entreprise 
#
# !!! ==> A FAIRE !!!
#
#==============================================================================

def Get_description_entreprise_SOC(Soup):
#    myTest = str(mySoup.find_all('div', attrs = {'class':"infoEntity"})[1].span.contents[0])
    myTest = str(Soup.find_all('div', attrs = {'id':"EmpBasicInfo"}))
    #..........................................
    #..
    #... coder eventuellement des choses ici
    #.......
    #..........................................
    if (myTest == []) : 
        Result = 'NULL'
    else:
        Soup2 = Soup(myTest, 'lxml')
        myTxtTmp = str(Soup2.find_all('div', attrs = {'class':""})[2])
        myTxtTmp1 = re.sub(r'(.*)data-full="(.*).<br/>(.*)', r'\2', myTxtTmp)
        Result = myTxtTmp1
    return(Result)

#print(Get_description_entreprise_SOC(mySoup))




#==============================================================================
#-- Création du script des métadonnées descriptives
#==============================================================================
from bs4 import BeautifulSoup
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
        
        doc_id = file[-16:-8]
        value = []
        if type == "INFO-SOC":
            field = ["company", "city", "nb_employee", "company_description","type"]
            value.append(Get_nom_entreprise_SOC(mySoup))
            value.append(Get_ville_entreprise_SOC(mySoup))
            value.append(Get_taille_entreprise_SOC(mySoup))
            value.append(Get_description_entreprise_SOC(mySoup))
            value.append("INFO-SOC")
        elif type == "AVIS-SOC":
            field = ["company","avg_rating","type"]
            value.append(Get_nom_entreprise_AVI(mySoup))
            value.append(Get_note_moy_entreprise_AVI(mySoup))
            value.append("AVIS-SOC")
        else:
            field = ["lib_job","company","city", "job_description","type"]
            value.append(Get_libelle_emploi_EMP(mySoup))
            value.append(Get_nom_entreprise_EMP(mySoup))
            value.append(Get_ville_emploi_EMP(mySoup))
            value.append(Get_texte_emploi_EMP(mySoup))
            value.append("INFO-EMP")
        for i, column in enumerate(field) :
            metadata.append([doc_id,column,value[i]])
            
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