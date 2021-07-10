import numpy as np
from skimage import io

import datetime

import scipy.ndimage

""" 
Une entreprise doit suivre la température et l'humidité de ses locaux
tous les quarts d'heures. En attendant l'installation d'eqpt connectés
permettant la remonté directe des valeurs vers un serveur dédié, chaque
salarié est chargé de prendre en photo l'horloge numérique présente sur
son bureau. Cette dernière affiche l'heure, l'humidité et la température.

L'entreprise vous sollicite pour analyser chaque image et d'en extraire
les informations utiles. Seules 2 images ont été fournies par l'entreprise :
http://acabani.free.fr/python2/horloge1.jpg
http://acabani.free.fr/python2/horloge2.jpg

Ce qui est attendu :
- Un rapport de quelques pages qui :
   - Explique notre démarche
   - Présente les différentes fonctions avec illustrations de leur utilisation
   - Difficultés rencontrées
   - Conclusion et limites de votre solution
- Code Python de votre programme au format .py

Aucune bibliothèque dédiée au traitement d'images ne doit être utilisée.
"""

def progression(i,nb_i):
    progress = int(np.trunc(100*i/(nb_i)))
    print("Progression : " + str(progress) + "% . ", end="\r")



# Génération de l'image à traité

img_originale = io.imread('horloge1.jpg')
#img_originale = io.imread("horloge2.jpg")
img= np.copy(img_originale)
io.imshow(img)
io.show()

# Traitement de l'image pour la convertir en image binaire :

def img2gray(image):
    longueur = image.shape[0]
    hauteur = image.shape[1]
    pixels = image.shape[2]
    result = np.ndarray(shape=(longueur,hauteur), dtype=np.float64)
    print(result.shape)
    for i in range(0,longueur):
        for j in range(0,hauteur): #  R                          G                           B
            result[i][j] = (image[i][j][0] * 0.92) + (image[i][j][1] * 0.04) + (image[i][j][2] * 0.04)
        
        progression(i,longueur)
    return result

img_gray = img2gray(img)

io.imshow(img_gray, cmap="gray")
io.show()

def filter(img,matrice,coef = 1): # On envoie la matrice en paramètre et le coef de celle-ci
    result = np.copy(img) 
    longueur = img.shape[0]
    hauteur = img.shape[1]
    
    for i in range(1,longueur-1): # On ignore les extrémités des lignes
        for j in range(1,hauteur-1): # et celles des colonnes
            if np.ndim(img) == 2 : # Pour les images 2 dimensions (Noir & Blanc)
                matPixel = np.array([ [ img[i-1][j-1],img[i-1][j],img[i-1][j+1] ],
                                    [ img[i][j-1],img[i][j],img[i][j+1] ],
                                    [ img[i+1][j-1],img[i+1][j],img[i+1][j+1] ] ])
                matRes = matPixel * matrice
                result[i][j] = np.sum(matRes) * coef
        progression(i,longueur-1)
    return result

maMatrice = np.array([[ 5,-25, 5],
                      [-25, -10,-25],
                      [ 5,-25, 5]])
img_filtree = filter(img_gray,maMatrice, 3)

io.imshow(img_filtree, cmap="gray")
io.show()
print()


def zoomOut(img,zoom):
    result = np.copy(img) 
    result = scipy.ndimage.zoom(result, 1/zoom, mode='constant')
    return result

img_zoom = zoomOut(img_filtree, 5)
io.imshow(img_zoom, cmap="gray")
io.show()
print()

def binary_filter(img, seuil):
    result = np.copy(img) 
    longueur = img.shape[0]
    hauteur = img.shape[1]
    # Si l'image n'est pas de bonne dimension, on sort
    if np.ndim(img) != 2 :
        return None 
    
    for i in range(0,longueur): 
        for j in range(0,hauteur): 
                if img[i][j] > seuil :
                    result[i][j] = 1
                else :
                    result[i][j] = 0
        progression(i,longueur)
    return result


img_binaire = binary_filter(img_zoom,-34000)
io.imshow(img_binaire, cmap="gray")
io.show()
print()

print("Sauvegarde de l'image binaire sous le nom \"img_binaire.jpg\"")
io.imsave("img_binaire.jpg",img_binaire)






# Analyse de l'image





img = io.imread("img_binaire.jpg")


#np.set_printoptions(threshold=1000) #will revert it to default behaviour
#np.set_printoptions(threshold=np.inf)
#print(img)

print(img.shape)

#########################################################################

NB0 = np.array([
    [1, 1, 0, 0, 0, 1, 1],
    [1, 0, 1, 1, 1, 0, 1],
    [1, 0, 1, 1, 1, 0, 1],
    [1, 0, 1, 1, 1, 0, 1],
    [1, 0, 1, 1, 1, 0, 1],
    [1, 0, 1, 1, 1, 0, 1],
    [1, 0, 1, 1, 1, 0, 1],
    [1, 0, 1, 1, 1, 0, 1],
    [1, 1, 0, 0, 0, 1, 1]
])
NB1 = np.array([
    [1, 1, 1, 1, 1, 0, 0],
    [1, 1, 1, 1, 1, 0, 0],
    [1, 1, 1, 1, 1, 0, 0],
    [1, 1, 1, 1, 1, 0, 0],
    [1, 1, 1, 1, 1, 0, 0],
    [1, 1, 1, 1, 1, 0, 0],
    [1, 1, 1, 1, 1, 0, 0],
    [1, 1, 1, 1, 1, 0, 0],
    [1, 1, 1, 1, 1, 0, 0]
]) 
# Le 2 a été redessiné pour changer la diagonale  en barres droites
NB2 = np.array([
    [1, 1, 0, 0, 0, 1, 1],
    [1, 1, 1, 1, 1, 0, 1],
    [1, 1, 1, 1, 1, 0, 1],
    [1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 1, 1],
    [0, 1, 1, 1, 1, 1, 1],
    [0, 1, 1, 1, 1, 1, 1],
    [0, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 1, 1]
])
NB3 = np.array([
    [1, 1, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 0, 1],
    [1, 1, 1, 1, 1, 0, 1],
    [1, 1, 1, 1, 1, 0, 1],
    [1, 1, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 0, 1],
    [1, 1, 1, 1, 1, 0, 1],
    [1, 1, 1, 1, 1, 0, 1],
    [1, 1, 0, 0, 0, 0, 1]
])
NB4 = np.array([
    [1, 0, 1, 1, 1, 0, 1],
    [1, 0, 1, 1, 1, 0, 1],
    [1, 0, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 0, 1],
    [1, 1, 1, 1, 1, 0, 1],
    [1, 1, 1, 1, 1, 0, 1],
    [1, 1, 1, 1, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 1]
])
NB5 = np.array([
    [1, 1, 0, 0, 0, 0, 1],
    [1, 1, 0, 1, 1, 1, 1],
    [1, 1, 0, 1, 1, 1, 1],
    [1, 1, 0, 1, 1, 1, 1],
    [1, 1, 0, 0, 0, 1, 1],
    [1, 1, 1, 1, 1, 0, 1],
    [1, 1, 1, 1, 1, 0, 1],
    [1, 1, 1, 1, 1, 0, 1],
    [1, 1, 0, 0, 0, 1, 1]
])
NB6 = np.array([
    [1, 1, 1, 0, 0, 0, 1],
    [1, 1, 0, 1, 1, 1, 1],
    [1, 1, 0, 1, 1, 1, 1],
    [1, 1, 0, 1, 1, 1, 1],
    [1, 1, 0, 0, 0, 1, 1],
    [1, 1, 0, 1, 1, 0, 1],
    [1, 1, 0, 1, 1, 0, 1],
    [1, 1, 0, 1, 1, 0, 1],
    [1, 1, 0, 0, 0, 1, 1]
])
NB7 = np.array([
    [1, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 0, 1],
    [1, 1, 1, 1, 1, 0, 1],
    [1, 1, 1, 1, 0, 1, 1],
    [1, 1, 1, 0, 1, 1, 1],
    [1, 1, 1, 0, 1, 1, 1],
    [1, 1, 0, 1, 1, 1, 1],
    [1, 1, 0, 1, 1, 1, 1],
    [1, 0, 1, 1, 1, 1, 1]
]) 
# Le 8 a été redessiné car les images ont toutes un "8" un peu penché
NB8 = np.array([
    [1, 1, 1, 0, 0, 0, 0],
    [1, 1, 0, 1, 1, 1, 0],
    [1, 1, 0, 1, 1, 1, 0],
    [1, 1, 0, 1, 1, 1, 0],
    [1, 1, 0, 0, 0, 0, 1],
    [1, 1, 0, 1, 1, 0, 1],
    [1, 1, 0, 1, 1, 0, 1],
    [1, 1, 0, 1, 1, 0, 1],
    [1, 1, 0, 0, 0, 1, 1]
])
NB9 = np.array([
    [1, 1, 0, 0, 0, 1, 1],
    [1, 0, 1, 1, 1, 0, 1],
    [1, 0, 1, 1, 1, 0, 1],
    [1, 0, 1, 1, 1, 0, 1],
    [1, 1, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 0, 1],
    [1, 1, 1, 1, 1, 0, 1],
    [1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 1, 1]
])

def zoomIn(img,zoom):

    result = scipy.ndimage.zoom(img, zoom, mode='constant')
    return result

# Un bon zoom progressif devra avoir un pas de 0.1


def isGoodSuperposition(img,img_NB,posX,posY,black_pixel_on_NB, white_pixel_on_NB):
    result = np.copy(img)

    longueur_NB = img_NB.shape[0]
    
    milieu = int(longueur_NB/2)

    hauteur_NB = img_NB.shape[1]

    #print("("+str(longueur_NB)+","+str(hauteur_NB)+")")

    black_pixel_on_Superposition = 0
    white_pixel_on_Superposition = 0

    # Ajout 08/06/2021, si il détecte pas de pixel noir sur
    # la ligne au milieu du rectangle du chiffre, il sort
    no_black_pixel = True
    for i in range(posY, posY+hauteur_NB):
        if result[posX+milieu][i] < 20 :
            no_black_pixel = False
    if no_black_pixel == True :
        return False


    for i in range(posX,posX+longueur_NB):
        for j in range(posY,posY+hauteur_NB):
                                
            # On compte le nombre de pixels blanc présent dans ce rectangle
            if result[i][j] > 220 : # S'il est vraiment blanc :
                white_pixel_on_Superposition = 1 + white_pixel_on_Superposition
                                
            # On superpose l'image avec le chiffre pour voir si les pixels restent noir
            result[i][j] = result[i][j] + img_NB[i-posX][j-posY] * 255 
                                            # *255 car l'image de NB varie de 0 à 1
            if result[i][j] < 20 : #si la superposition reste noire
                black_pixel_on_Superposition =  1 + black_pixel_on_Superposition
    
    # Si plus de 92% des pixels noirs et blancs se superposent bien
    #print("on_Superposition : " + str(black_pixel_on_Superposition))
    if black_pixel_on_Superposition >= 0.92*black_pixel_on_NB and white_pixel_on_Superposition >= 0.92*white_pixel_on_NB :
        return True
    else :
        return False

def Matching(img, img_NB, number = None, zoom = None):

    liste_NB_presents = np.empty(shape=[0, 0, 0])

    longueur = img.shape[0]
    hauteur = img.shape[1]
    longueur_NB = img_NB.shape[0]
    hauteur_NB = img_NB.shape[1]

    black_pixel_on_NB = 0
    white_pixel_on_NB = 0

    for i in range(0,longueur_NB):
        for j in range(0,hauteur_NB):
            if img_NB[i][j] < 0.1 : # Si le pixel est noir
                black_pixel_on_NB = black_pixel_on_NB + 1
            elif img_NB[i][j] > 0.9 : # Si le pixel est blanc
                white_pixel_on_NB = white_pixel_on_NB + 1


    print("Nb pixels noirs sur l'image \"NB"+str(number)+" Zoom("+str(zoom)+")\" : " + str(black_pixel_on_NB))
    print("Nb pixels blancs sur l'image \"NB"+str(number)+" Zoom("+str(zoom)+")\" : " + str(white_pixel_on_NB))

    #  De la colonne 0 à la colonne longueur max - longueur du nombre
        # Pour aller plus vite, on avance de 2 pixels en 2 pixels, 
        # 3 en 3 c'est trop large et on loupe des superpositions
    for i in range(0, longueur - longueur_NB  ,  2):
        for j in range(0, hauteur - hauteur_NB  ,  2):

            if isGoodSuperposition( img, img_NB, i, j, black_pixel_on_NB, white_pixel_on_NB ) == True :
                print("   - L'image se superpose bien en : (" + str(i)+","+str(j)+")")
                # On ajoute à la fois les coordos i (x) et j (y) dans notre array
                # Ainsi que le numéro du chiffre et le coefficient du zoom
                liste_NB_presents =np.append(liste_NB_presents,[number,i,j,zoom])
        
        progression(i,longueur-longueur_NB)
    
    return liste_NB_presents


# Analyse :
def Matching_By_Number(img,number, minZoom = 1.5, maxZoom = 2.3, iZoom = 0.1):

    liste_NB = np.empty(0)
    for zoom in np.arange(minZoom, maxZoom+iZoom, iZoom):
        zoom = np.round(zoom,1)

        NB_zoom = zoomIn(eval("NB"+str(number)), zoom)
        
        liste_NB = np.append(liste_NB, Matching(img, NB_zoom, number, zoom)  )
    
    return liste_NB.reshape(int(liste_NB.size/4), 4)


# ANALYSE FINALE : 

def All_Matching(img, NB_debut = 0, NB_fin = 9, minZoom = 1.5, maxZoom = 2.3, iZoom = 0.1):
    liste_all_NB = np.empty(0)
    for i in range(NB_debut, NB_fin +1 ):
        liste_all_NB = np.append(liste_all_NB,Matching_By_Number(img,i, minZoom, maxZoom, iZoom))
        liste_all_NB = liste_all_NB.reshape(int(liste_all_NB.size/4), 4)

    print("Liste de tous les chiffres identifiées, leurs coordonnées X,Y et le zoom")
    print(liste_all_NB)    
    
    return liste_all_NB



# Ecriture sur l'image des zones identifiées

def addBorder(img,width):
    # Ajout de la bordure
    return np.pad(img,(width, width), 'constant', constant_values=(0.2))


def addImage(img1,img2,posX,posY):
    result = np.copy(img1)

    img2 = addBorder(img2,1)
    #img2 = replaceByBorder(img2,1)

    longueur2 = img2.shape[0]
    hauteur2 = img2.shape[1]

    for i in range(posX,posX+longueur2):
        for j in range(posY,posY+hauteur2):
            result[i][j] = img2[i-posX-longueur2][j-posY-hauteur2] *255
    return result


def addNB(img1,number,posX,posY, zoom):

    img2 = zoomIn(eval("NB"+str(int(number))), zoom)

    result = addImage(img1,img2, posX, posY)

    return result


def Replace_Matching(img,liste_all_NB):

    for i in range(0, liste_all_NB.shape[0]):
        number = int(liste_all_NB[i][0])
        x = int(liste_all_NB[i][1])
        y = int(liste_all_NB[i][2])
        zoom = liste_all_NB[i][3]
        img_identifying = addNB(img,number, x, y, zoom)
        io.imshow(img_identifying)
        io.show()


#Replace_Matching(img, All_Matching(img, 0, 9, 1.3, 2.0, 0.1))
Replace_Matching(img, All_Matching(img, 0, 9, 1.5, 2.3, 0.1))

#print(Matching_By_Number(img,2))
#print(Matching(img,NB2_zoom))

#img = addImage(img,NB2_zoom,30,70)
#io.imshow(img)
#io.show()

#print(img)

print()
print("Fin du traitement")
