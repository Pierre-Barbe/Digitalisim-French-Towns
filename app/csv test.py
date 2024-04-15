import csv
import math
import requests

# Transfer list
l_transfer = []

# Department correspondance list
dict_departement = {'1' : 'Ain', '2' : 'Aisne', '3' : 'Allier', '4' : 'Alpes-de-Haute-Provence', '5' : 'Hautes-Alpes', '6' : 'Alpes-Maritimes', '7' : 'Ardèche',
                    '8' : 'Ardennes', '9' : 'Ariège', '10' : 'Aube', '11' : 'Aude', '12' : 'Aveyron', '13' : 'Bouches-du-Rhône', '14' : 'Calvados', '15' : 'Cantal',
                    '16' : 'Charente', '17' : 'Charente-Maritime', '18' : 'Cher', '19' : 'Corrèze', '200' : 'Corse-du-Sud', '201' : 'Corse-du-Sud', '202' : 'Haute-Corse',
                    '206' : 'Haute-Corse', '21' : 'Côte-d Or', '22' : 'Côtes-d Armor', '23' : 'Creuse', '24' : 'Dordogne', '25' : 'Doubs', '26' : 'Drôme', '27' : 'Eure',
                    '28' : 'Eure-et-Loir', '29' : 'Finistère', '30' : 'Gard', '31' : 'Haute-Garonne', '32' : 'Gers', '33' : 'Gironde', '34' : 'Hérault', '35' : 'Ille-et-Vilaine',
                    '36' : 'Indre', '37' : 'Indre-et-Loire', '38' : 'Isère', '39' : 'Jura', '40' : 'Landes', '41' : 'Loir-et-Cher', '42' : 'Loire', '43' : 'Haute-Loire',
                    '44' : 'Loire-Atlantique', '45' : 'Loiret', '46' : 'Lot', '47' : 'Lot-et-Garonne', '48' : 'Lozère', '49' : 'Maine-et-Loire', '50' : 'Manche', '51' : 'Marne',
                    '52' : 'Haute-Marne', '53' : 'Mayenne', '54' : 'Meurthe-et-Moselle', '55' : 'Meuse', '56' : 'Morbihan', '57' : 'Moselle', '58' : 'Nièvre', '59' : 'Nord',
                    '60' : 'Oise', '61' : 'Orne', '62' : 'Pas-de-Calais', '63' : 'Puy-de-Dôme', '64' : 'Pyrénées-Atlantiques', '65' : 'Hautes-Pyrénées', '66' : 'Pyrénées-Orientales',
                    '67' : 'Bas-Rhin', '68' : 'Haut-Rhin', '69' : 'Rhône', '70' : 'Haute-Saône', '71' : 'Saône-et-Loire', '72' : 'Sarthe', '73' : 'Savoie', '74' : 'Haute-Savoie',
                    '75' : 'Paris', '76' : 'Seine-Maritime', '77' : 'Seine-et-Marne', '78' : 'Yvelines', '79' : 'Deux-Sèvres', '80' : 'Somme', '81' : 'Tarn', '82' : 'Tarn-et-Garonne',
                    '83' : 'Var', '84' : 'Vaucluse', '85' : 'Vendée', '86' : 'Vienne', '87' : 'Haute-Vienne', '88' : 'Vosges', '89' : 'Yonne', '90' : 'Territoire de Belfort',
                    '91' : 'Essonne', '92' : 'Hauts-de-Seine', '93' : 'Seine-Saint-Denis', '94' : 'Val-de-Marne', '95' : 'Val-d Oise', '971' : 'Guadeloupe', '972' : 'Martinique',
                    '973' : 'Guyane', '974' : 'La Réunion', '975' : 'Saint-Pierre-et-Miquelon', '976' : 'Mayotte', '977' : 'Saint-Barthélemy', '978' : 'Saint-Martin',
                    '984' : 'Terres australes et antarctiques françaises', '986' : 'Wallis-et-Futuna', '987' : 'Polynésie française', '988' : 'Nouvelle-Calédonie',
                    '989' : 'Île de Clipperton', '98' : 'Alpes-Maritimes'}

# Downloading from specified URL and writing to Test file
r = requests.get('https://www.data.gouv.fr/fr/datasets/r/dbe8a621-a9c4-4bc3-9cae-be1699c5ff25', allow_redirects=True)
open('app/Test download.csv', 'wb').write(r.content)

# Database Extraction
with open('app/Test download.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)

    #Looping through rows
    for row in reader:

        # Computing Department Number
        cp = int(row['code_postal'])
        if (cp > 96000 and cp != 98000) or (cp>=20000 and cp < 21000):
            departement = math.floor(cp/100)
        else :
            departement = math.floor(cp/1000)

        # Extracting relevant values and preparing rows for custom Database
        line = {'code_postal': row['code_postal'], 'nom_commune_complet': row['nom_commune_complet'].upper(), 'departement': dict_departement[str(departement)]}
        l_transfer.append(line)

# Database Writing
with open('app/BDD Digitalisim.csv', 'w', newline='') as csvfile:
    fieldnames = ['code_postal', 'nom_commune_complet', 'departement']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for row in l_transfer:
        writer.writerow(row)
