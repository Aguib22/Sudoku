
from  fonction_classe import *
from  interface import *



# Programme principal
if __name__ == "__main__":
    sudoku = Sudoku()
    UserInterface.empty_grid()
    while True:

        UserInterface.home_menu()
        choice_input = input(">>> ")
        if choice_input == '1':
            level = input("Entrez le Niveau >>>  ")
            exist, grid_sudoku, resolve = Sudoku.choice_of_sudoku(level)
            convert, grids = Sudoku.generate_grid(grid_sudoku)
            conv, g_resolved = Sudoku.generate_grid(resolve)
            grid_orig = deepcopy(grids)
            Sudoku.shwo_grid(grid_orig)

            UserInterface.game_option()
            choice_game = input(">>> ")
            if choice_game == '1':
                Sudoku.shwo_grid(g_resolved)

            elif choice_game == '2':
                while Sudoku.fin_jeu(grids):

                   p, v = Sudoku.user_input("")
                   suplement, grid = Sudoku.fill_empty_box(grids, grid_orig, p, v)
                   if (p,v) == (None,None):
                       break
                   else:
                       if suplement:
                           print('ajout autorisé')
                       else:
                           print("ajout non autorisé")
                   Sudoku.shwo_grid(grids)

                if Sudoku.comparaison(grids,g_resolved):
                    print("______________________________")
                    print('  Bravo vous avez gagnez')
                    print("______________________________")
                else:
                    print("______________________________")
                    print("   desolé vous avez perdu:!")
                    print("______________________________")



        elif choice_input == '2':

            nom_fichier = input("Entrez le nom du fichier pour sauvegarder la grille générée : ")
            exist, grid_sudoku, resolve = Sudoku.choice_of_sudoku("facile")
            converti, grids = Sudoku.generate_grid(grid_sudoku)
            with open(nom_fichier,"w") as fichier:

                for l in grids:
                     fichier.write(str(l))
            conv, g_resolved = Sudoku.generate_grid(resolve)
            grid_orig = deepcopy(grids)
            Sudoku.shwo_grid(grid_orig)

            UserInterface.game_option()
            choice_game = input(">>> ")
            if choice_game == '1':
                Sudoku.generate_grid(g_resolved)

            elif choice_game == '2':
                while  Sudoku.fin_jeu(grids):

                    p, v = Sudoku.user_input("")

                    suplement, grille = Sudoku.remplire_case_vide(grids, grid_orig, p, v)

                    if (p, v) == (None, None):
                        break
                    else:
                        if suplement:
                            print('ajout autorisé')
                        else:
                            print("ajout non autorisé")

                    Sudoku.shwo_grid(grids)

                if Sudoku.comparaison(grid, g_resolved):
                    print("______________________________")
                    print('  Bravo vous avez gagnez')
                    print("______________________________")
                else:
                    print("______________________________")
                    print("   desolé vous avez perdu:!")
                    print("______________________________")

            # Code pour sauvegarder la grille générée dans un fichier
        elif choice_input == '3':
            break
        else:
            print("Choix invalide. Veuillez choisir une option valide.")







