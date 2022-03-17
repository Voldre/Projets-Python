import matplotlib.pyplot as plt 
import matplotlib.image as mpimg 
import numpy as np

import matplotlib.ticker as mtick

import cv2

print(cv2.__version__)

"""
███████ ██   ██  ██████  ███████      ██ 
██       ██ ██  ██    ██ ██          ███ 
█████     ███   ██    ██ ███████      ██ 
██       ██ ██  ██    ██      ██      ██ 
███████ ██   ██  ██████  ███████      ██ 
                                         
                                         
                                        """

#img = mpimg.imread("Eden_img.jpg")
img = cv2.imread("Eden_img.jpg") #,0) pour l'afficher en gris

img_1canal = cv2.imread("Eden_img.jpg",0)

#print("all : ",img)
#print("black & white : ",img_1canal)

#imgplot = plt.imshow(img)
cv2.imshow('Mon image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('EdenGrey.png',img_1canal) # Sauvegarder l'image en noir et blanc




"""
███████ ██   ██  ██████  ███████     ██████  
██       ██ ██  ██    ██ ██               ██ 
█████     ███   ██    ██ ███████      █████  
██       ██ ██  ██    ██      ██     ██      
███████ ██   ██  ██████  ███████     ███████ 
                                             
                                             """


#print(x)
"""
plt.hist(img, range=(0, 10), bins = 5, color = "yellow", edgecolor = "red")
plt.title("test")
plt.show()
"""

hist1 = cv2.calcHist([img], [0], None, [256], [1, 256])
hist2 = cv2.calcHist([img_1canal], [0], None, [256], [1,256])

#print(hist1)
#print(hist2)

fig, ax = plt.subplots()

plt.subplot(311)
plt.title("Histogramme de l'image en couleur")
plt.hist(hist1, range = (0,256), color = "blue")
plt.plot(hist1)


plt.subplot(312)
# Equivalence en histogramme bâton

liste_hist = []

for i in range(len(hist1)) : # 0 à 255 couleurs
    for j in range( int(hist1[i]) ): # 0 à la valeur de hist[i] (donc 0 à 3000)
        liste_hist.append( i ) # on ajoute dans la liste l'absisse, donc i (0 à 255)
    # Si on a 5 pixels à la valeur grise 10, 2 pixels à la valeur 11 et 3 à 12, on aura :
    # [10,10,10,10,10,11,11,12,12,12] etc...

plt.title("Histogramme bâton de l'image en couleur")

plt.hist(liste_hist, range = (0,256), color = "blue", bins = 256, edgecolor = "black")
                        # 0 à 256 valeurs   ,        256 bâtons

plt.subplot(313)
#x = [1,2,2,3,4,4,4,4,5,5]
#print(img_1canal)
#print(hist)

liste_valeurs = []
for i in range(len(hist2)) : # 0 à 255 couleurs
    for j in range( int(hist2[i]) ): # 0 à la valeur de hist[i] (donc 0 à 3000)
        liste_valeurs.append( i ) # on ajoute dans la liste l'absisse, donc i (0 à 255)

plt.hist(liste_valeurs, range = (0,256), facecolor='grey', bins = 256, edgecolor = "black")

plt.title("Histogramme bâton de l'image en noir et blanc")


plt.savefig("Histogramme.png")
plt.show()


"""
███████ ██   ██  ██████  ███████     ██████  
██       ██ ██  ██    ██ ██               ██ 
█████     ███   ██    ██ ███████      █████  
██       ██ ██  ██    ██      ██          ██ 
███████ ██   ██  ██████  ███████     ██████  
                                             
                                             """

"""
 ██████ 
██      
██      
██      
 ██████   
        """
def Histo_Cumul(hist,mycolor="", mytitle="", image_name=""):
    
    fig, ax = plt.subplots()
    liste_hist_cumul = []

    nb_value = 0

    for i in range(len(hist)) : # 0 à 255 couleurs
        hist[i] = hist[i] // 50 
        # // 50 Pour raccourir la liste de valeurs (car même les plus petites valeurs font 100 occurences )
        nb_value += hist[i]
        for j in range( int(nb_value) ): # 0 à la valeur de hist[i] (donc 0 à 3000)
            liste_hist_cumul.append( i ) # on ajoute dans la liste l'absisse, donc i (0 à 255)
        # Si on a 5 pixels à la valeur grise 10, 2 pixels à la valeur 11 et 3 à 12, on aura :
        # [10,10,10,10,10,11,11,12,12,12] etc...

    plt.title(mytitle)

    plt.hist(liste_hist_cumul, range = (0,256), color = mycolor, bins = 256, edgecolor = "black")
                            # 0 à 256 valeurs   ,        256 bâtons
    ax.yaxis.set_major_formatter(mtick.PercentFormatter(xmax = int(nb_value) ))

    fig.savefig(image_name)
    plt.show()

    """
    plt.subplot(212)
    plt.title("Histogramme de l'image en noir et blanc")
    plt.hist(hist2, range = (0,256), color = "grey")
    plt.plot(hist2)
    """
Histo_Cumul(hist1,"blue","Histogramme Cumulé Normalisé de l'image en couleur","Histogramme_Cumule.png")

"""
██████  
██   ██ 
██   ██ 
██   ██ 
██████      
        """
Histo_Cumul(hist2,"grey","Histogramme Cumulé Normalisé de l'image en gris","Histogramme_Cumule_Gris.png")


# hist1 = cv2.calcHist([img], [0], None, [256], [1, 256])
# hist2 = cv2.calcHist([img_1canal], [0], None, [256], [1,256])


"""
███████ ██   ██  ██████  ███████     ███████ ██ ██   ████████ ██████  ███████ ███████ 
██       ██ ██  ██    ██ ██          ██      ██ ██      ██    ██   ██ ██      ██      
█████     ███   ██    ██ ███████     █████   ██ ██      ██    ██████  █████   ███████ 
██       ██ ██  ██    ██      ██     ██      ██ ██      ██    ██   ██ ██           ██ 
███████ ██   ██  ██████  ███████     ██      ██ ███████ ██    ██   ██ ███████ ███████ 
                                                                                      
"""
image_moyenneur = cv2.blur(img, (3, 3))

cv2.imshow("Filtre Moyenneur", image_moyenneur)

image_median = cv2.medianBlur(img,3)

cv2.imshow("Filtre Median", image_median)

ecarttype = 1

image_gaussien = cv2.GaussianBlur(img, (3,3), ecarttype)

cv2.imshow("Filtre Gaussien", image_gaussien)

cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('Moyenneur.png',image_moyenneur) 
cv2.imwrite('Median.png',image_median) 
cv2.imwrite('Gaussien.png',image_gaussien) 
