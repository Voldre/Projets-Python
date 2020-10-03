# http://patorjk.com/software/taag/#p=display&f=ANSI%20Regular&t=EXOS%2012

# 2)
import matplotlib
import matplotlib.pyplot as plt
#import matplotlib.image as mpimg
#from PIL import Image
import numpy as num
import numpy as np

#import random2

import scipy
import scipy.signal as signal # Obliger de déclarer scipy.signal même si scipy est déclaré
import scipy.integrate as integrate


# Fonction Affichage


def affichage(mytitle,numero, s1, s2 = "", s3 = ""):

    fig, ax = plt.subplots()
    
    if s3 == "" :
        if s2 == "" :
            plt.plot(s1)
            plt.title(mytitle)
        else:
            plt.subplot(211)
            plt.title(mytitle)
            #plt.axis([0, 1, -2, 2])
            plt.xlabel('Time [seconds]')

            if len(s1) == 2 :
                plt.plot(s1[0],s1[1]) #Composé des éléments x pour [0] et y pour [1]
            else:
                plt.plot(s1)
            plt.subplot(212)
            if len(s2) == 2 :
                plt.plot(s2[0],s2[1]) #Composé des éléments x pour [0] et y pour [1]
            else:
                plt.plot(s2)
    else:
            if numero == "7bis" :
                plt.subplot(311)
                plt.title(mytitle)
                plt.plot(s1,"-o")
                plt.subplot(312)
                #plt.title(mytitle)
                plt.plot(s2,"-o")
                plt.subplot(313)
                plt.plot(s3,"-o")
            else:
                plt.subplot(311)
                plt.title(mytitle)
                plt.plot(s1)
                plt.subplot(312)
                #plt.title(mytitle)
                plt.plot(s2)
                plt.subplot(313)
                plt.plot(s3)

        #plt.legend(['sin','cos','sin+cos'], loc=3) 
    #plt.set(xlabel='temps (s)',ylabel='tension (mV)',title= mytitle )

    fig.savefig("ex_"+str(numero)+".png")
    plt.show()
                        # Pas Te = 0.01s


"""
███████ ██   ██  ██████  ███████      ██ 
██       ██ ██  ██    ██ ██          ███ 
█████     ███   ██    ██ ███████      ██ 
██       ██ ██  ██    ██      ██      ██ 
███████ ██   ██  ██████  ███████      ██ 
                                         
                                         
                                        """

f1 = 5
f2 = 30

F = 2000
T = 1/F
t = num.arange(0.0, 1, T) 
#t = num.linspace(0, 1, 1000, False)  # 1 second

s = num.sin(2 * num.pi * f1 * t) + num.sin(2 * num.pi * f2 * t)

# BP = [fc,inf]
fc = 25
#fc fréquence de coupure du filtre passe haut : 25Hz


sos = signal.cheby1(10, 2, fc, 'hp', fs=2000, output='sos')
                    #rp = 2
# rp :float The maximum ripple allowed below unity gain in the passband. Specified in decibels, as a positive number.


            #order #attenuat° dB, fc #Wn, #Filtre type, freq echantillonage

filtered = signal.sosfilt(sos, s)

affichage('Exos 1 : After 25 Hz high-pass filter with Chebyshev Type I',1,s,filtered)

"""
Wn !: array_like
    A scalar or length-2 sequence giving the critical frequencies. For Type II filters, this is the point in the transition band at which the gain first reaches -rs.

    For digital filters, Wn are in the same units as fs. By default, fs is 2 half-cycles/sample, so these are normalized from 0 to 1, where 1 is the Nyquist frequency. (Wn is thus in half-cycles / sample.)

    For analog filters, Wn is an angular frequency (e.g., rad/s).
"""

"""
███████ ██   ██  ██████  ███████     ██████  
██       ██ ██  ██    ██ ██               ██ 
█████     ███   ██    ██ ███████      █████  
██       ██ ██  ██    ██      ██     ██      
███████ ██   ██  ██████  ███████     ███████ 
                                             
                                             """


sosTypeII = signal.cheby2(10, 20, fc, 'highpass', fs=2000, output='sos')
                    #cheby2   #rs = 20
    #rs float The minimum attenuation required in the stop band. Specified in decibels, as a positive number.


filtered_II = signal.sosfilt(sosTypeII, s)

affichage('Exos 2 : After 25 Hz high-pass filter with Chebyshev Type II',2,s,filtered_II)

"""
███████ ██   ██  ██████  ███████     ██████  
██       ██ ██  ██    ██ ██               ██ 
█████     ███   ██    ██ ███████      █████  
██       ██ ██  ██    ██      ██          ██ 
███████ ██   ██  ██████  ███████     ██████  
                                             
                                             """

sosButter = signal.butter(10, fc, 'hp', fs=2000, output='sos')
                    #no attribute rp or rs

filtered_Butter = signal.sosfilt(sosButter, s)

affichage('Exos 3 : After 25 Hz high-pass filter with Butterworth',3,s,filtered_Butter)


"""
███████ ██   ██  ██████  ███████     ██   ██ 
██       ██ ██  ██    ██ ██          ██   ██ 
█████     ███   ██    ██ ███████     ███████ 
██       ██ ██  ██    ██      ██          ██ 
███████ ██   ██  ██████  ███████          ██ 
                                             
                                             """

sosCauer = signal.ellip(10, 2, 20, fc, 'hp', fs=2000, output='sos')
                    #rp = 2 and rs = 20

filtered_Cauer = signal.sosfilt(sosCauer, s)

affichage('Exos 4 : After 25 Hz high-pass filter with Cauer',4,s,filtered_Cauer)

"""
███████ ██   ██  ██████  ███████     ███████ 
██       ██ ██  ██    ██ ██          ██      
█████     ███   ██    ██ ███████     ███████ 
██       ██ ██  ██    ██      ██          ██ 
███████ ██   ██  ██████  ███████     ███████ 
                                             
                                             """
"""

"""
"""
███████ ██   ██  ██████  ███████      ██████  
██       ██ ██  ██    ██ ██          ██       
█████     ███   ██    ██ ███████     ███████  
██       ██ ██  ██    ██      ██     ██    ██ 
███████ ██   ██  ██████  ███████      ██████  
                                              
                                              """

T0 = 0.001
Fe = 1/T0

f0 = 5

t = num.arange(-2.0, 2.0, T0) 
#t = num.linspace(0, 1, 1000, False)  # 1 second

s = ( num.sin(num.pi * f0 * t) ) / ( num.pi * t)

affichage('Exos 6 : Signal x(t)',6,s)

"""
███████ ██   ██  ██████  ███████     ███████ 
██       ██ ██  ██    ██ ██               ██ 
█████     ███   ██    ██ ███████         ██  
██       ██ ██  ██    ██      ██        ██   
███████ ██   ██  ██████  ███████        ██   
                                             
                                             """

# Fréquence d'échantillonage
Fe = [20,6,30]


""" Méthode 1 """
# Shannon :  Fe > 2Fmax
sortie = [[],[],[]]

for x, index in zip(Fe , range( len(Fe) )) :
    sortie.append([index])
    for i, j in zip(range( len(t) ) , t) :
        #print(i," et ",1/i)
        #print(i)
        if i % x != 0:
            sortie[index].append(0)
        else:
            sortie[index].append(   (num.sin(num.pi * f0 * j) ) / ( num.pi * j) )

affichage("Exercice 7 : Echantillonnage à 20, 6 et 30Hz",7,sortie[0],sortie[1],sortie[2])

""" Méthode 2 """

t = []

signals = []

for x, index in zip(Fe, range( len(Fe) )) :
    t.append( num.arange(-2.0, 2.0, 1/x)  )

    signals.append( ( num.sin(num.pi * f0 * t[index]) ) / ( num.pi * t[index]) )



affichage("Exercice 7 : Echantillonnage à 20, 6 et 30Hz","7bis",signals[0],signals[1],signals[2])

"""
L'échantillonnage doit vérifier la condition de Shannon, à savoir Fe >= 2 * F

"""

"""
███████ ██   ██  ██████  ███████      █████  
██       ██ ██  ██    ██ ██          ██   ██ 
█████     ███   ██    ██ ███████      █████  
██       ██ ██  ██    ██      ██     ██   ██ 
███████ ██   ██  ██████  ███████      █████  
                                             
                                             """
