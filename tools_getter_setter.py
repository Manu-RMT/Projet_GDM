import pandas as pd
import re

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


#==============================================================================
#-- LINKEDIN (EMPLOI) : Nombre d'employé
#==============================================================================
def Get_nb_empl(Soup):
    myTest = Soup.find_all('span', attrs={'class': 'num-applicants__caption'})
    if (myTest == []):
        Result = 'NULL'
    else:
        myTest = str(myTest[0].text)
        if (myTest == []):
            Result = 'NULL'
        else:
            Result = myTest
    return (Result)

#==============================================================================
#-- LINKEDIN (EMPLOI) : Date de publication
#==============================================================================
def Get_date_publication(Soup):
    myTest = Soup.find_all('span', attrs={'class': 'topcard__flavor--metadata posted-time-ago__text'})
    if (myTest == []):
        Result = 'NULL'
    else:
        myTest = str(myTest[0].text)
        if (myTest == []):
            Result = 'NULL'
        else:
            Result = myTest
    return (Result)

#==============================================================================
#-- LINKEDIN (EMPLOI) : Niveau hiérarchique
#==============================================================================
def Get_niveau_hierarchique(Soup):
    try:
        niveau_hierarchique = Soup.find('h3', string='Niveau hiérarchique').find_next('span',
                                                                                      class_='job-criteria__text').text
        Result = niveau_hierarchique.strip()
    except AttributeError:
        Result = 'NULL'

    return Result


#==============================================================================
#-- LINKEDIN (EMPLOI) : Type d'emploi
#==============================================================================
def Get_type_emploi(Soup):
    try:
        type_emploi = Soup.find('h3', string='Type d’emploi').find_next('span', class_='job-criteria__text').text
        Result = type_emploi.strip()
    except AttributeError:
        Result = 'NULL'

    return Result


#==============================================================================
#-- LINKEDIN (EMPLOI) : Fonction
#==============================================================================
def Get_fonction(Soup):
    try:
        fonction = Soup.find('h3', string='Fonction').find_next('span', class_='job-criteria__text').text

        Result = fonction.strip()
    except AttributeError:
        Result = 'NULL'

    return Result


#==============================================================================
#-- LINKEDIN (EMPLOI) : Secteurs
#==============================================================================
def Get_secteurs(Soup):
    try:
        secteurs = Soup.find('h3', string='Secteurs').find_next('span', class_='job-criteria__text').find_all_next(
            'span', class_='job-criteria__text')

        secteurs_text = ''.join(secteur.text.strip() for secteur in secteurs)
        Result = secteurs_text
    except AttributeError:
        Result = 'NULL'

    return Result


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
def Get_nom_entreprise_SOC(Soup):
    myTest = Soup.find_all('h1', attrs = {"strong tightAll"})[0].span.contents[0]

    if (myTest == []) :
        Result = 'NULL'
    else:
        myTxtTmp = str(myTest)
        Result = re.sub(r'(.*)<h1 class="strong tightAll" data-company="(.*)" title="">(.*)', r'\2', myTxtTmp)
    return(Result)



#==============================================================================
#-- GLASSDOOR (SOCIETE) : Fonction renvoyant la ville de l'entreprise
#==============================================================================

def Get_ville_entreprise_SOC(Soup):
    type_donne = str(Soup.find_all('div', attrs = {'class':"infoEntity"})[1].label.contents[0])

    if type_donne != "Siège social":
        myTest = []
    else:
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
    type_donne = str(Soup.find_all('div', attrs = {'class':"infoEntity"})[1].label.contents[0])

    if type_donne != "Siège social":
        myTest = str(Soup.find_all('div', attrs = {'class':"infoEntity"})[1].span.contents[0])
    else:
        myTest = str(Soup.find_all('div', attrs = {'class':"infoEntity"})[2].span.contents[0])

    if (myTest == []) :
        Result = 'NULL'
    else:
        myTxtTmp = str(myTest)
        myTxtTmp1 = re.sub(r'(.*)<h1 class=" strong tightAll" data-company="(.*)" title="">(.*)', r'\2', myTxtTmp)
        Result = myTxtTmp1
    return(Result)


#==============================================================================
#-- GLASSDOOR (SOCIETE) : Date de fondation
#==============================================================================
def Get_FONDES_entreprise_SOC(Soup):
    trouve = False
    for i in range(1, 8):
        if trouve == True:
            continue
        type_donne = str(Soup.find_all('div', attrs={'class': "infoEntity"})[i].label.contents[0])
        print(type_donne)
        if type_donne == "Fondé en":
            myTest = str(Soup.find_all('div', attrs={'class': "infoEntity"})[i].span.contents[0])
            trouve = True

    if (myTest == []) :
        Result = 'NULL'
    else:
        myTxtTmp = str(myTest)
        myTxtTmp1 = re.sub(r'(.*)<h1 class=" strong tightAll" data-company="(.*)" title="">(.*)', r'\2', myTxtTmp)
        Result = myTxtTmp1
    return(Result)

#==============================================================================
#-- GLASSDOOR (SOCIETE) : Fonction renvoyant le type de l'entreprises
#==============================================================================
def Get_type_entreprise_SOC(Soup):
    # E1127781_P1
    trouve=False
    for i in range(1,8):
        if trouve == True:
            continue
        type_donne = str(Soup.find_all('div', attrs={'class': "infoEntity"})[i].label.contents[0])
        if type_donne == "Type":
            myTest = str(Soup.find_all('div', attrs={'class': "infoEntity"})[i].span.contents[0])
            trouve=True

    if (myTest == []) :
        Result = 'NULL'
    else:
        myTxtTmp = str(myTest)
        myTxtTmp1 = re.sub(r'(.*)<h1 class=" strong tightAll" data-company="(.*)" title="">(.*)', r'\2', myTxtTmp)
        Result = myTxtTmp1
    return(Result)

#==============================================================================
#-- GLASSDOOR (SOCIETE) : Fonction renvoyant le secteur d'activité de l'entreprise
#==============================================================================
def Get_secteur_entreprise_SOC(Soup):
    trouve = False
    for i in range(1, 8):
        if trouve == True:
            continue
        type_donne = str(Soup.find_all('div', attrs={'class': "infoEntity"})[i].label.contents[0])
        if type_donne == "Secteur":
            myTest = str(Soup.find_all('div', attrs={'class': "infoEntity"})[i].span.contents[0])
            trouve = True

    if (myTest == []) :
        Result = 'NULL'
    else:
        myTxtTmp = str(myTest)
        myTxtTmp1 = re.sub(r'(.*)<h1 class=" strong tightAll" data-company="(.*)" title="">(.*)', r'\2', myTxtTmp)
        Result = myTxtTmp1
    return(Result)




#==============================================================================
#-- GLASSDOOR (SOCIETE) : Fonction renvoyant la description de l'entreprise 
#==============================================================================

def Get_description_entreprise_SOC(Soup):
    myTest = Soup.find_all('div', attrs = {'class':"margTop empDescription"})
    if (myTest == []) : 
        Result = 'NULL'
    else:
        myTxtTmp = str(myTest)
        match = re.search(r'data-full="([^"]+)"', myTxtTmp)
        if match:
            myTxtTmp1 = match.group(1)
        # myTxtTmp1 = re.sub(r'(.*)data-full="(.*).<br/>(.*)', r'\2', myTxtTmp)
        Result = myTxtTmp1
    return(Result)



#==============================================================================
#-- Retourne le chemin du fichier en fonction du type
#==============================================================================
def get_html_links_csv(csv,type):
    data = pd.read_csv(csv, delimiter=';')
        
    types = data[data.colonne=='type_du_fichier']
    types = types[types.valeur==type]
    html_links = pd.merge(data, types, how="inner", on=["cle_unique","cle_unique"])
    html_links = html_links[html_links.colonne_x=='lien_fichier']
    html_links = html_links["valeur_x"]
    return html_links
