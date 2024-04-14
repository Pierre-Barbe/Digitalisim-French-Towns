import csv
import math
with open('app/communes-departement-region.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['code_postal'], row['nom_commune_complet'].upper(), math.floor(int(row['code_postal'])/1000))
