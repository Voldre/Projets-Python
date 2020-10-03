# http://patorjk.com/software/taag/#p=display&f=ANSI%20Regular&t=EXOS%2012

# 2)
import matplotlib
import matplotlib.pyplot as plt
#import matplotlib.image as mpimg
#from PIL import Image
import numpy as num

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
            if len(s1) == 2 :
                plt.plot(s1[0],s1[1]) #Composé des éléments x pour [0] et y pour [1]
            else:
                plt.plot(s1)
            plt.subplot(212)
            if len(s1) == 2 :
                plt.plot(s2[0],s2[1]) #Composé des éléments x pour [0] et y pour [1]
            else:
                plt.plot(s2)
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

t = num.arange(-4.0, 4.0, 0.01) 


def Draw_Door(T,origin):


    x0 = -2*T + origin # Pour décaler
    y0 = 0
    x0b = -T/2 + origin
    y0b = 0
    x1 = -T/2 + origin
    y1 = 1
    x2 = T/2 + origin
    y2 = 1
    x3 = T/2 + origin
    y3 = 0
    x3b = 2*T + origin # Pour décaler
    y3b = 0

    x_values = [x0,x0b,x1,x2,x3,x3b]
    y_values = [y0,y0b,y1,y2,y3,y3b]

    return x_values,y_values

"""
    #fig, plt = plt.subplots()

    plt.xlabel('temps (s)')
    plt.ylabel('tension (mV)')
    plt.title('Question 2')
    plt.grid()
    #plt.savefig("ex_2.png")

    plt.show()
"""

#large = input("Saisissez la largeur de la porte : ")
#large = int(large)

T = 2

origin = -1

# Début et fin de la porte
t1 = origin - T/2
t2 = origin + T/2

#Door = Draw_Door(T,0)#large)

def Draw_Door2(T,origin):
    Porte = []

    for i in t :
        if i >= t1 and i <= t2 :
            Porte.append(1)
        else:
            Porte.append(0)
    return Porte

Door = Draw_Door2(T,origin)

s = num.exp(-t)

affichage("Question 2",2,Door,s)


"""
███████ ██   ██  ██████  ███████     ██████  
██       ██ ██  ██    ██ ██               ██ 
█████     ███   ██    ██ ███████      █████  
██       ██ ██  ██    ██      ██          ██ 
███████ ██   ██  ██████  ███████     ██████  
                                             
                                             """

s2 = 2 * num.exp(-t)

correl = num.correlate(s,Door,mode='full')

convol = num.convolve(s,Door,mode='full')

#print("Question 3, correlation : ",correl,", convolution : ",convol)

affichage("Question 3 : Correlation et Convolution avec la formule",3,correl,convol)


A = 1 # Amplitude porte
a = 1 # coef de exp(-at) ?
z1 = (A/a)*(1-num.exp(-a*(t-t1)))
z2 = ( A*num.exp(-a*t) / a ) * (num.exp(a*t2 - a*t1))
#z22 = ( A*num.exp(-a*t) / a ) * (num.exp(a*t2) - num.exp(a*t1) )

#z3 = (A/a)*(1 - num.exp(-a*(t2-t1)))

#z = z1+z2

z = []

for i in t :
    if i < t1 :
        z.append(0)
    if t1 < i < t2 :
        z.append( (A/a)*(1-num.exp(-a*(i-t1)))  )
    elif i > t2 :
        z.append(  ( A*num.exp(-a*i) / a ) * (num.exp(a*t2) - num.exp(a*t1) )  )


affichage("Question 3 - suite : Correlation et Convolution à la main","3bis",z1,z2,z) # Avec z
#affichage("",99,z3)


"""
███████ ██   ██  ██████  ███████     ██   ██ 
██       ██ ██  ██    ██ ██          ██   ██ 
█████     ███   ██    ██ ███████     ███████ 
██       ██ ██  ██    ██      ██          ██ 
███████ ██   ██  ██████  ███████          ██ 
                                             
                                             """

sLT1 = [ 1000, 100, 10]
sLT2 = [ 0.0001, 0.01, 1]

s = signal.lti(sLT1,sLT2)

x1, y1 = signal.step(s)
x2, y2 = signal.impulse(s)

fig, ax = plt.subplots()

plt.title("Exercice 4 : Réponse du système LTI ")
plt.plot(x1,y1,"green")
plt.plot(x2,y2,"blue")
fig.savefig("ex_4.png")
plt.show()

# INVITE DE COMMANDE :  cd .. permet de REMONTER d'un niveau!