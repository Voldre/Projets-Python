#    Select the lines you want to unindent, and
#    use Ctrl + ] to unindent them.
import matplotlib.pyplot as plt 
import matplotlib.image as mpimg 
import numpy as np

import cv2

def Affichage_Sauvegarde(titre,image) :
    cv2.imshow(titre,image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    votre_nom = input("Saisissez le nom sous lequel enregistrer l'image (0 annule l'enregistrement) : ")
    if votre_nom == "0" or None :
        print("...")
    else :
        votre_nom = votre_nom + ".png"
        cv2.imwrite(votre_nom,image)

def Edition(image,cmd) :
        #image = image2
        print("")
        if cmd == 5 :
            my_color = input("Quelle couleur souhaitez-vous modifier (R,G,B) : ")
            my_color = my_color.upper()
            if my_color == "R" : my_color = 2
            elif my_color == "G" or my_color == "V" : my_color = 1
            elif my_color == "B" : my_color = 0
            else : 
                return 0,0

        choice = input("Souhaitez vous augmenter (AUG) ou diminuer (DIM) ? : ")
        choice = choice.upper()

        for i in range( len(image) ) :
            for j in range( len(image[i]) ) :
                for color in range( len(image[i][j])) :
                    if cmd == 3:
                        if choice == "AUG" :
                            if image[i][j][color] <= 225:
                                image[i][j][color] += 30
                            else:
                                image[i][j][color] = 255
                        elif choice == "DIM" :
                            if image[i][j][color] >= 60:
                                image[i][j][color] -= 60
                            else:
                                image[i][j][color] = 0
                        # Cas où ni AUG ni DIM géré dans le code même
                    if cmd == 4:
                        if choice == "AUG" :
                            if 30 <= image[i][j][color] <= 128:
                                image[i][j][color] -= 30
                            elif image[i][j][color] < 30:
                                image[i][j][color] = 0
                            elif 129 <= image[i][j][color] <= 225 :
                                image[i][j][color] += 30
                            else :
                                image[i][j][color] = 255

                        elif choice == "DIM" :
                            if image[i][j][color] <= 103:
                                image[i][j][color] += 25
                            elif 104 <= image[i][j][color] <= 153:
                                image[i][j][color] = 128 # Tout au centre
                            else :
                                image[i][j][color] -= 25
                if cmd == 5:
                    if choice == "AUG" :
                        if image[i][j][my_color] <= 225 :
                            image[i][j][my_color] += 30
                        else :
                            image[i][j][my_color] = 255
                    elif choice == "DIM" :
                        if image[i][j][my_color] >= 30 :
                            image[i][j][my_color] -= 30
                        else :
                            image[i][j][my_color] = 0


                        
        return image, choice



while 1 :
    print("Bienvenue dans l'application d'édition d'image.")
    print("Vous allez pouvoir choisir l'image que vous souhaitez éditer, \npour cela, collez ici le réportoire de l'image suivi du nom complet,\nExemple : C:\Mon_PC\Documents\Mon_Dossier\mon_image.png")
    nom_image = input("Saisissez-le ici : ")

 # Insertion/Chargement de l'image

    if nom_image.find(".png") != -1 or nom_image.find(".jpg") != -1 :
        image = cv2.imread(nom_image)
        if image is None :
            print("Erreur : Le répertoire saisi ne correspond pas à une image valide, revoyez le répertoire")
            break
        image_load = True
        cv2.imshow('Mon image',image)
        cv2.imwrite('mon_image.png',image) # Sauvegarder l'image
        cv2.waitKey(0)
        cv2.destroyAllWindows()


    else:
        print("Erreur : Le répertoire saisi ne correspond pas à une image valide (en .png ou .jpg)")

# Liste du Menu

    while image_load :

        liste = nom_image.split("\\")
        nom = liste[len(liste)-1]
        print("Vous travaillez sur l'image \"",nom,"\"")

        print("- - - - - - - - - - - - - - - -")
        print("Vous voici dans le menu, plusieurs options se présentent à vous, saisissez :")
        print("0 : Pour changer d'image")
        print("1 : Pour sauvegarder votre image en noir et blanc")
        print("2 : Pour récupérer les contours de l'image")
        print("3 : Pour augmenter ou diminuer la luminosité")
        print("4 : Pour augmenter ou diminuer le contraste")
        print("5 : Pour augmenter ou diminuer une couleur")
        print("6 : Pour pixeliser l'image")
        print("7 : Pour redimensionner l'image")
        print("8 : Flouter l'image")
        print("9 : Augmenter la netteté de l'image")
        print("10 : Effectuer une rotation de l'image")

#   Liste des Commandes

        cmd = input("Votre saisie : ")
        cmd = int(cmd)

        if cmd == 0 :
            image_load = False
        if cmd == 1 :
            tempo = cv2.imread("mon_image.png",0)
            Affichage_Sauvegarde("Image noir et blanc",tempo)
            
        elif cmd == 2 :

            choice = input("Souhaitez-vous récupérer les contours en couleur (C) ou en noir et blanc (NB) ? : ")
            kernel = np.ones((6,6), np.uint8)
            choice = choice.upper()
            if choice == "NB" :
                tempo = cv2.imread("mon_image.png",0)
                tempo = cv2.morphologyEx(tempo, cv2.MORPH_GRADIENT, kernel)

            elif choice == "C" :
                tempo = cv2.morphologyEx(image, cv2.MORPH_GRADIENT, kernel)
            Affichage_Sauvegarde("Contours de l'iamge",tempo)

        elif cmd == 3 :
            tempo = image
            tempo, choice = Edition(image,cmd)

            if choice == "AUG" :
                Affichage_Sauvegarde("Luminosité Augmentée",tempo)
            elif choice == "DIM" :
                Affichage_Sauvegarde("Luminosité Diminuée",tempo)
            else :
                print("Erreur : Mauvaise saisie, AUG ou DIM était attendu.\n")

        elif cmd == 4 :
            tempo, choice = Edition(image,cmd)
            if choice == "AUG" :
                Affichage_Sauvegarde("Contraste Augmentée",tempo)
            elif choice == "DIM" :
                Affichage_Sauvegarde("Contraste Diminuée",tempo)
            else :
                print("Erreur : Mauvaise saisie, AUG ou DIM était attendu.\n")

        elif cmd == 5 :
            tempo, choice = Edition(image,cmd)
            if choice == "AUG" :
                Affichage_Sauvegarde("Couleur Augmentée",tempo)
            elif choice == "DIM" :
                Affichage_Sauvegarde("Couleur Diminuée",tempo)
            else :
                print("")
                if tempo == 0:
                    print("Erreur : Mauvaise saisie, R, G ou B était attendu.")
                print("Erreur : Mauvaise saisie, AUG ou DIM était attendu.\n")

        elif cmd == 6 or cmd == 7 :
            height, width = image.shape[:2]
            new_width = input("Saisissez la largeur de l'image en nombre de pixels : ")
            new_width = int(new_width)
            if new_width <= 0 :
                print("Erreur, vous n'avez pas saisie une quantité de pixels valide.")
            
            ratio = new_width / width
            new_height = height * ratio
            new_height = int(new_height)
            # Redimensionne l'image
            if cmd == 6 :
                output = cv2.resize(image, (new_width, new_height), interpolation=cv2.INTER_LINEAR)
            if cmd == 7 :
                output = cv2.resize(image, (new_width, new_height), interpolation=cv2.INTER_NEAREST)
            
            fig, ax = plt.subplots()
            ax = plt.subplot(211)
            plt.title("Entrée")
            #plt.imshow(tempo) # Couleur inversé, "BGR"
            plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
            ax = plt.subplot(212)
            plt.title("Sortie")
            plt.imshow(cv2.cvtColor(output, cv2.COLOR_BGR2RGB))
            
            plt.show()

            votre_nom = input("Saisissez le nom sous lequel enregistrer l'image (0 annule l'enregistrement) : ")
            if votre_nom == "0" or None :
                print("...")
            else :
                nom2 = votre_nom + "2"
                votre_nom += ".png"
                fig.savefig(votre_nom)
                nom2 += ".png"
                cv2.imwrite(nom2,output)

        elif cmd == 8 :
            tempo = image
            value = input("Saisissez à quel point vous voulez flouter l'image (de 1 à 100) :")
            value = int(value)
            if value <= 0 or value is None :
                print("Erreur : vous n'avez pas saisie une valeur valide.")
            else :
                image_moyenneur = cv2.blur(tempo, ( 1+value*2 , 1+value*2))
                Affichage_Sauvegarde("Image floutée",image_moyenneur)

        elif cmd == 9:
            kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
            image = cv2.filter2D(image, -1, kernel)
            Affichage_Sauvegarde("Image Nette",image)

        elif cmd == 10 :
            rows,cols, ch = image.shape

            angle = input("Saisissez de combien de degré vous voulez tourner l'image (ex : 90, 180, 270) : ")
            angle = int(angle)
            if angle <= 0:
                angle = angle % 360

            M = cv2.getRotationMatrix2D((cols/2,rows/2),angle,1)
            image = cv2.warpAffine(image,M,(cols,rows))

            Affichage_Sauvegarde("Output",image)

       #  if cmd == 11 : Symétrie

        else :
           print("Erreur : La commande saisie est invalide.")
           print("")