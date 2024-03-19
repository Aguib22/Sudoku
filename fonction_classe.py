from string import  ascii_lowercase
from  copy import deepcopy
from  random import randint



class Sudoku:
    """
        definition de la classe Sudoku
        il s'agit de la classe dans la quelle est définie les methodes pour la résolution
        de cet exercice de sukoku

    """

    def shwo_grid(grid):
        #cette fonction permet juste d'affiche une grille

        indice_alpha = "abcdefghi"
        print("    a b c   d e f   g h i")
        for indice_line, line in enumerate(grid):
            if indice_line % 3 == 0:
                print(" ", ('+' + '-' * 7) * 3 + '+')
            print(indice_alpha[indice_line], end=' ')
            for col in range(len(line)):
                if col % 3 == 0:
                    print('|', end=" ")
                print(line[col], end=" ")


            print('|')
        print(" ", ('+' + '-' * 7) * 3 + '+')

    def generate_grid(chaine):
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
        grid_sudoku = []
        line = []
        for i, elem in enumerate(chaine):
            line.append(int(elem))

            if (i + 1) % 9 == 0:
                grid_sudoku.append(line)
                line = []
        return True, grid_sudoku

    def fill_empty_box(grid, grid_orig, cord, val):
        """
        description:
            la fonction qui permet de remplire les cases de la grille par l'utilisateur
        parms:
            grid: la grille que l'utilisateur doit remplir
            grid_orig: c'est la copie de la grille qui permettra de verifie si une case doit etre modifiée ou pas
            cord: prend les cordonnées de la case à remplire
            val: prend la valeurs de la case


        """
        if val not in range(0, 10):
            return False, grid

        row = ascii_lowercase.index(cord[1])
        line = ascii_lowercase.index(cord[0])
        if line > 8:
            return False, grid
        disp = False
        if grid_orig[line][row] == 0:
            disp = True

        if not disp:
            return False, grid

        grid[line][row] = val
        return True, grid

    def user_input(self):
        """
        description:
            cette fonction permet de prendre la saisie de l'utilisateur
        retours:
            elle retourne les cordonnées et la valeur de la case


        """
        msg_err = ""
        check_input = False
        while not check_input:
            check_input = True
            input_coordinate = input("donner les cordonnées de la case à modifier sous le format [a b] ou taper 'q' pour sortir:")

            if input_coordinate.lower() == 'q':

                return None, None  # Retourne None pour indiquer à l'appelant que l'utilisateur veut quitter

            if len(input_coordinate) != 3:
                check_input = False
                msg_err = "donner le bon format de saisi"
            else:
                line_cord = input_coordinate[0]
                indice_possible = 'abcdefghi'
                if line_cord not in indice_possible:
                    check_input = False
                    msg_err = f"les cordonnés doivent etre dans {indice_possible}"
                else:
                    row_cord = input_coordinate[2]
                    if row_cord not in indice_possible:
                        check_input = False
                        msg_err = f"les cordonnés doivent etre dans {indice_possible}"

            if check_input:
                cordonnee = [line_cord, row_cord]
            else:
                print(msg_err)

        # saisie de la valeur
        check_input = False
        msg_err = ""
        while not check_input:
            check_input = True
            input_value = (input("donner la valeur de la cellule:"))

            if input_value not in "123456789":
                check_input = False
                msg_err = "la valeur doit etre comprise entre 0 et 9"

            if check_input:
                value = int(input_value)
            else:
                print(msg_err)

        return cordonnee, value


    def loading_file(level):
        """
        description:
            cette fonction est chargée de faire la manipulation des fichiers pour choisir une chaine
            de grille en fonction du niveau de jeu choisi par l'utilisateur
        params:
            level: le niveau de jeu choisi par le user
        retour:
            un bollen qui indique si la chaine est bein chargée ou pas
            liste_sudoku: la chaine de sudoku en frome de liste
            liste_sudoku_resolu: la resolution de la chaine liste_sudoku
        """
        file_path = {
            'facile': "file_of_sudoku/facile.txt",
            'moyen': 'file_of_sudoku/moyen.txt',
            'difficile': 'file_of_sudoku/difficile.txt'
        }
        resolution_fil_path = {
            'facile': 'file_sudoku_resolved/R_facile.txt',
            'moyen': 'file_sudoku_resolved/R_moyen.txt',
            'difficile': 'file_sudoku_resolved/R_difficile.txt'
        }
        if level not in file_path:
            return False, None,None
        file = open(file_path[level], "r")
        content = file.read()
        file.close()
        fic = open(resolution_fil_path[level], "r")
        content_resolved = fic.read()
        fic.close()

        list_sudoku = content.split('\n')
        list_resolved_sudoku = content_resolved.split('\n')
        return True, list_sudoku, list_resolved_sudoku

    def choice_of_sudoku(level):
        """
        description:
            cette fonction a pour role de choisir de façon aleatoire la chaine de sudoku
        params:
            level: le niveau de jeu choisi par le user
        retours:
            un booleen qui retourne l'état du choisi
            content[indice_grid]: la grille
            resolve[indice_grid]:la solution de la grille

        """

        exist, content, resolve = Sudoku.loading_file(level)

        if not exist:
            return False, None,None

        indice_grid = randint(0, len(content) - 1)

        return True, content[indice_grid], resolve[indice_grid]

    def fin_jeu(grid):
        #cette fonction retourne l'état du jeu "terminé ou pas"
        zero=0
        for line in grid:
            for item in line:
                if item == 0:
                  zero +=1
        if zero > 0:
            return True

        else:
            return False

    def comparaison(user_grid,g_resolve):
        """
        celle ci compare la grille apres que l'utilisateur aies fini de remplire et
        la solution de grille  pour verifier si le user a gagner ou perdu en respectant le principe du sudoku
        """

        return g_resolve == user_grid


