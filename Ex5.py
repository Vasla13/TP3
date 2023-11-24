heure_debut = int(input("Donnez l'heure de début de la location (un entier) : "))
heure_fin = int(input("Donnez l'heure de fin de la location (un entier) : "))

if heure_debut < 0 or heure_fin > 24 or heure_debut >= heure_fin:
    if heure_debut < 0 or heure_debut > 24 or heure_fin < 0 or heure_fin > 24:
        print("Les heures doivent être comprises entre 0 et 24 !\n")
    elif heure_debut == heure_fin:
        print("Attention ! L'heure de fin est identique à l'heure de début.\n")
    else:
        print("Attention ! L'heure de début de la location est après l'heure de fin.\n")
else:
    duree_location = heure_fin - heure_debut

    if 0 <= heure_debut < 7 or 17 <= heure_debut <= 24:
        tarif = 1.0
    else:
        tarif = 2.0

    print(f"Vous avez loué votre vélo pendant {duree_location} heure(s) au tarif horaire de {tarif} euro(s).")
    montant_total = duree_location * tarif
    print(f"Le montant total à payer est de {montant_total} euro(s).")
