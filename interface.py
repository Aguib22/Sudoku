class InterfaceUtilisateur:
    @staticmethod
    def afficher_accueil():
        print("Bienvenue ! Que souhaitez-vous faire ?")
        print("1. Chargement d'une grille")
        print("2. Génération d'une grille")
        print("3. Quitter")

    @staticmethod
    def mini_accueil():
        print("0. Jouer")
        print("1. Chargement d'une grille")
        print("2. Génération d'une grille")

    @staticmethod
    def afficher_options_jeu():
        print("1. Résolution")
        print("2. Interactif")

    @staticmethod
    def grille_vide():
        indice_alpha = "abcdefghi"
        print("    a b c   d e f   g h i")
        for indice_line in range(0, 9):
            if indice_line % 3 == 0:
                print(" ", ('+' + '-' * 7) * 3 + '+')
            print(indice_alpha[indice_line], end=' ')
            for col in range(9):
                if col % 3 == 0:
                    print('|', end=" ")
                print('0', end=" ")

            print('|')
        print(" ", ('+' + '-' * 7) * 3 + '+')
