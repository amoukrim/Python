# Daily challenge GOLD : Happy birthday
# On importe deux modules :
# datetime pour manipuler les dates, calendar pour vérifier les années bissextiles
from datetime import datetime
import calendar

# 🔹 Étape 1 : Demander la date de naissance à l'utilisateur
# L'utilisateur doit entrer la date au format jour/mois/année
birthdate_str = input("Entrez votre date de naissance (format JJ/MM/AAAA) : ")

# 🔹 Étape 2 : Convertir la chaîne de caractères en objet datetime
birthdate = datetime.strptime(birthdate_str, "%d/%m/%Y")

# 🔹 Étape 3 : Calculer l’âge de l'utilisateur
today = datetime.today()  # Obtenir la date d'aujourd'hui
age = today.year - birthdate.year  # Calcul de base : année actuelle - année de naissance

# Si l'anniversaire de l'utilisateur n'est pas encore passé cette année, on enlève 1
if (today.month, today.day) < (birthdate.month, birthdate.day):
    age -= 1

# 🔹 Étape 4 : Trouver le dernier chiffre de l’âge pour le nombre de bougies
last_digit = age % 10  # Ex: 53 → 3 bougies

# 🔹 Étape 5 : Vérifier si l'utilisateur est né une année bissextile
leap = calendar.isleap(birthdate.year)  # Renvoie True si l'année est bissextile

# 🔹 Étape 6 : Définir une fonction pour afficher le gâteau avec les bougies
def print_cake(candles):
    """
    Affiche un gâteau d'anniversaire avec un certain nombre de bougies.
    :param candles: le nombre de 'i' représentant les bougies sur le gâteau
    """
    print("     ___" + "i" * candles + "___")  # ligne avec les bougies
    print("    |:H:a:p:p:y:|")                 # décoration texte "Happy"
    print("  __|___________|__")              # base du haut du gâteau
    print(" |^^^^^^^^^^^^^^^^^|")            # décoration
    print(" |:B:i:r:t:h:d:a:y:|")            # texte "Birthday"
    print(" |                 |")            # espace vide
    print(" ~~~~~~~~~~~~~~~~~~~\n")          # base du gâteau

# 🔹 Étape 7 : Affichage final selon année bissextile ou non
if leap:
    print("🎉 Vous êtes né(e) une année bissextile ! Deux gâteaux pour vous \n")
    print_cake(last_digit)  # Premier gâteau
    print_cake(last_digit)  # Deuxième gâteau
else:
    print_cake(last_digit)  # Un seul gâteau