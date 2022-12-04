import random

# declare les variable
niveau_vie = 20
numero_adversaire = 0
numero_combat = 0
nombre_victoires = 0
nombre_defaites = 0
combat_statut = ""
nombre_victoires_consecutives = 0


# fonction main du jeu, elle est appeller quand on a besoin d'un nouveau monstre dans une partie
def main():
    global niveau_vie, numero_adversaire, numero_combat, nombre_victoires, nombre_defaites, combat_statut, \
        nombre_victoires_consecutives  # declare les variable globale
    force_adversaire = random.randint(1, 5)  # choisi un nombre entre 1 et 5 pour la force de l'adversaire
    numero_adversaire += 1

    print("Vous tombez face à face avec un adversaire de difficulté :", force_adversaire)

    choix = int(input("Que voulez-vous faire ? \n1- Combattre cet adversaire\n2- Contourner cet adversaire et aller "
                      "ouvrir "
                      "une autre porte\n3- Afficher les règles du jeu\n4- Quitter la partie\n"))

    if choix == 1:
        numero_combat += 1
        score_dé = random.randint(1, 6)  # choisi un nombre entre 1 et 6 pour l'attaque du joueur
        print(
            f"\nAdversaire : {numero_adversaire}\nForce de l’adversaire : {force_adversaire}\nNiveau de vie de "
            f"l’usager : {niveau_vie}\nCombat {numero_combat} : {nombre_victoires} vs {nombre_defaites}\n")
        if score_dé > force_adversaire:  # si le joueur gagne
            combat_statut = "victoire"
            nombre_victoires += 1
            nombre_victoires_consecutives += 1
            niveau_vie += force_adversaire
            print(f"Lancer du dé : {score_dé}")
            print(f"Dernier combat = {combat_statut}")
            print(
                f"Niveau de vie : {niveau_vie}\nNombre de victoires consécutives : {nombre_victoires_consecutives}\n")
            main()
        elif score_dé <= force_adversaire:  # si le joueur perd
            combat_statut = "défaite"
            nombre_defaites += 1
            nombre_victoires_consecutives = 0
            niveau_vie -= force_adversaire
            if niveau_vie < 0:  # fait que la vie ne soit pas negatif
                niveau_vie = 0
            print(f"Lancer du dé : {score_dé}")
            print(f"Dernier combat = {combat_statut}")
            print(f"Niveau de vie : {niveau_vie}\n")
            if niveau_vie <= 0:  # si la vie est 0 ou plus petit que 0, appelle la fonction de fin de jeu
                fin()
            main()

    elif choix == 2:
        niveau_vie -= 1
        print(f"\nok, vous avez perdu 1 point de vie\nNiveau de vie de l'usager: {niveau_vie}\n")
        if niveau_vie <= 0:  # si la vie est 0 ou plus petit que 0, appelle la fonction de fin de jeu
            fin()
        main()
    elif choix == 3:
        print(
            "\n2Pour réussir un combat, il faut que la valeur du dé lancé soit\n supérieure à la force de "
            "l’adversaire. "
            "Dans ce cas, le niveau\n de vie de l’usager est augmenté de la force de l’adversaire.\n Une défaite a "
            "lieu "
            "lorsque la valeur du dé lancé par l’usager\n est inférieure ou égale à la force de l’adversaire.  Dans "
            "ce\n "
            "cas, le niveau de vie de l’usager est diminué de\n la force de l’adversaire.\n\nLa partie se termine "
            "lorsque "
            "les points de vie de l’usager\n tombent sous 0.\n\nL’usager peut combattre ou éviter chaque adversaire, "
            "dans le\n cas de l’évitement, il y a une pénalité de 1 point de vie.\n")
        main()
    elif choix == 4:
        print("\nMerci et au revoir...\n")
        exit()


# fonction de fin de partie pour reinistaliser les variables
def fin():
    global niveau_vie, numero_adversaire, numero_combat, nombre_victoires, nombre_defaites, combat_statut, \
        nombre_victoires_consecutives
    print(f"La partie est terminée, vous avez vaincu {nombre_victoires} monstre(s).\n")
    niveau_vie = 20
    numero_adversaire = 0
    numero_combat = 0
    nombre_victoires = 0
    nombre_defaites = 0
    combat_statut = ""
    nombre_victoires_consecutives = 0
    main()


main()
