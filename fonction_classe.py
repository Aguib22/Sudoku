from string import  ascii_lowercase
from  copy import deepcopy
from  random import randint



class Sudoku:
    """
        definition de la classe Sudoku
        il s'agit de la classe dans la quelle est définie les methodes pour la résolution
        de cet exercice de sukoku

    """

    def affiche_grille(grille):
        #cette fonction permet juste d'affiche une grille

        indice_alpha = "abcdefghi"
        print("    a b c   d e f   g h i")
        for indice_line, line in enumerate(grille):
            if indice_line % 3 == 0:
                print(" ", ('+' + '-' * 7) * 3 + '+')
            print(indice_alpha[indice_line], end=' ')
            for col in range(len(line)):
                if col % 3 == 0:
                    print('|', end=" ")
                print(line[col], end=" ")


            print('|')
        print(" ", ('+' + '-' * 7) * 3 + '+')

    def generer_grille(chaine):
        """
        description:
            cette fonction a pour role de generer une grille de sudoku
        parms:
            chaine: il s'agie d'une chaine de 81 caractère que la fonction reçoit et la transforme en une grille
        retour:
            cette fonction retourne un booleen et une grille
        """
        if len(chaine) != 81:
            return False, None
        grille_sudoku = []
        ligne = []
        for i, elem in enumerate(chaine):
            ligne.append(int(elem))

            if (i + 1) % 9 == 0:
                grille_sudoku.append(ligne)
                ligne = []
        return True, grille_sudoku

    def remplire_case_vide(grille, grill_orig, cord, val):
        """
        description:
            la fonction qui permet de remplire les cases de la grille par l'utilisateur
        parms:
            grille: la grille que l'utilisateur doit remplir
            grill_orig: c'est la copie de la grille qui permettra de verifie si une case doit etre modifiée ou pas
            cord: prend les cordonnées de la case à remplire
            val: prend la valeurs de la case


        """
        if val not in range(0, 10):
            return False, grille

        col = ascii_lowercase.index(cord[1])
        ligne = ascii_lowercase.index(cord[0])
        if ligne > 8:
            return False, grille
        disp = False
        if grill_orig[ligne][col] == 0:
            disp = True

        if not disp:
            return False, grille

        grille[ligne][col] = val
        return True, grille

    def saisie_user(self):
        """
        description:
            cette fonction permet de prendre la saisie de l'utilisateur
        retours:
            elle retourne les cordonnées et la valeur de la case


        """
        msg_err = ""
        verif_saisie = False
        while not verif_saisie:
            verif_saisie = True
            saisie_cordonnee = input("donner les cordonnées de la case à modifier sous le format [a b]:")

            if saisie_cordonnee.lower() == 'q':

                return None, None  # Retourne None pour indiquer à l'appelant que l'utilisateur veut quitter

            if len(saisie_cordonnee) != 3:
                verif_saisie = False
                msg_err = "donner le bon format de saisi"
            else:
                line_cord = saisie_cordonnee[0]
                indice_possible = 'abcdefghi'
                if line_cord not in indice_possible:
                    verif_saisie = False
                    msg_err = f"les cordonnés doivent etre dans {indice_possible}"
                else:
                    col_cord = saisie_cordonnee[2]
                    if col_cord not in indice_possible:
                        verif_saisie = False
                        msg_err = f"les cordonnés doivent etre dans {indice_possible}"

            if verif_saisie:
                cordonnee = [line_cord, col_cord]
            else:
                print(msg_err)

        # saisie de la valeur
        verif_saisie = False
        msg_err = ""
        while not verif_saisie:
            verif_saisie = True
            valeur_saisie = (input("donner la valeur de la cellule:"))

            if valeur_saisie not in "123456789":
                verif_saisie = False
                msg_err = "la valeur doit etre comprise entre 0 et 9"

            if verif_saisie:
                valeur = int(valeur_saisie)
            else:
                print(msg_err)

        return cordonnee, valeur


    def fichier(niveau):
        """
        description:
            cette fonction est chargée de faire la manipulation des fichiers pour choisir une chaine
            de grille en fonction du niveau de jeu choisi par l'utilisateur
        params:
            niveau: le niveau de jeu choisi par le user
        retour:
            un bollen qui indique si la chaine est bein chargée ou pas
            liste_sudoku: la chaine de sudoku en frome de liste
            liste_sudoku_resolu: la resolution de la chaine liste_sudoku
        """
        chemin_fichier = {
            'facile': "facile.txt",
            'moyen': 'moyen.txt',
            'difficile': 'difficile.txt'
        }
        chemin_fichier_resolu = {
            'facile': 'R_facile.txt',
            'moyen': 'R_moyen.txt',
            'difficile': 'R_difficile.txt'
        }
        if niveau not in chemin_fichier:
            return False, None,None
        file = open(chemin_fichier[niveau], "r")
        contenu = file.read()
        file.close()
        fic = open(chemin_fichier_resolu[niveau], "r")
        contenu_resolu = fic.read()
        fic.close()

        liste_sudoku = contenu.split('\n')
        liste_sudoku_resolu = contenu_resolu.split('\n')
        return True, liste_sudoku, liste_sudoku_resolu

    def choix_chaine_sudoku(niveau):
        """
        description:
            cette fonction a pour role de choisir de façon aleatoire la chaine de sudoku
        params:
            niveau: le niveau de jeu choisi par le user
        retours:
            un booleen qui retourne l'état du choisi
            contenu[indice_grille]: la grille
            solution[indice_grille]:la solution de la grille

        """

        exist, contenu, solution = Sudoku.fichier(niveau)

        if not exist:
            return False, None,None

        indice_grille = randint(0, len(contenu) - 1)

        return True, contenu[indice_grille], solution[indice_grille]

    def fin_jeu(grille):
        #cette fonction retourne l'état du jeu "terminé ou pas"
        zero=0
        for line in grille:
            for elme in line:
                if elme == 0:
                  zero +=1
        if zero > 0:
            return True

        else:
            return False

    def comparaison(grille_user,g_resolue):
        """
        celle ci compare la grille apres que l'utilisateur aies fini de remplire et
        la solution de grille  pour verifier si le user a gagner ou perdu en respectant le principe du sudoku
        """

        return g_resolue == grille_user


