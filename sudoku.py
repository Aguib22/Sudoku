
from  fonction_classe import *
from  interface import *



# Programme principal
if __name__ == "__main__":
    sudoku = Sudoku()
    InterfaceUtilisateur.grille_vide()
    while True:

        InterfaceUtilisateur.afficher_accueil()
        choix = input(">>> ")
        if choix == '1':
            niveau = input("Entrez le Niveau >>>  ")
            exist, grille_sudoku, solution = Sudoku.choix_chaine_sudoku(niveau)
            converti, grilles = Sudoku.generer_grille(grille_sudoku)
            conv, g_resolu = Sudoku.generer_grille(solution)
            grille_orig = deepcopy(grilles)
            Sudoku.affiche_grille(grille_orig)

            InterfaceUtilisateur.afficher_options_jeu()
            choix_jeu = input(">>> ")
            if choix_jeu == '1':
                Sudoku.affiche_grille(g_resolu)

            elif choix_jeu == '2':
                while Sudoku.fin_jeu(grilles):

                   p, v = Sudoku.saisie_user("")
                   ajout, grille = Sudoku.remplire_case_vide(grilles, grille_orig, p, v)
                   if (p,v) == (None,None):
                       break
                   else:
                       if ajout:
                           print('ajout autorisé')
                       else:
                           print("ajout non autorisé")
                   Sudoku.affiche_grille(grilles)

                if Sudoku.comparaison(grille,g_resolu):
                    print("______________________________")
                    print('  Bravo vous avez gagnez')
                    print("______________________________")
                else:
                    print("______________________________")
                    print("   desolé vous avez perdu:!")
                    print("______________________________")



        elif choix == '2':

            nom_fichier = input("Entrez le nom du fichier pour sauvegarder la grille générée : ")
            exist, grille_sudoku, solution = Sudoku.choix_chaine_sudoku("facile")
            converti, grilles = Sudoku.generer_grille(grille_sudoku)
            with open(nom_fichier,"w") as fichier:

                for l in grilles:
                     fichier.write(str(l))
            conv, g_resolu = Sudoku.generer_grille(solution)
            grille_orig = deepcopy(grilles)
            Sudoku.affiche_grille(grille_orig)

            InterfaceUtilisateur.afficher_options_jeu()
            choix_jeu = input(">>> ")
            if choix_jeu == '1':
                Sudoku.affiche_grille(g_resolu)

            elif choix_jeu == '2':
                while  Sudoku.fin_jeu(grilles):

                    p, v = Sudoku.saisie_user("")

                    ajout, grille = Sudoku.remplire_case_vide(grilles, grille_orig, p, v)

                    if (p, v) == (None, None):
                        break
                    else:
                        if ajout:
                            print('ajout autorisé')
                        else:
                            print("ajout non autorisé")

                    Sudoku.affiche_grille(grilles)

                if Sudoku.comparaison(grille, g_resolu):
                    print("______________________________")
                    print('  Bravo vous avez gagnez')
                    print("______________________________")
                else:
                    print("______________________________")
                    print("   desolé vous avez perdu:!")
                    print("______________________________")

            # Code pour sauvegarder la grille générée dans un fichier
        elif choix == '3':
            break
        else:
            print("Choix invalide. Veuillez choisir une option valide.")







