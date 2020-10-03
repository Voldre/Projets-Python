import matplotlib
import matplotlib.pyplot as plt
#import matplotlib.image as mpimg
#from PIL import Image
import numpy as num

#import random2

import scipy
import scipy.integrate as integrate

# Fonction Affichage


def affichage(mytitle,numero, s1, s2 = "", s3 = ""):

    fig, ax = plt.subplots()

    if s2 != "":
        if numero == 4 :
            ax.plot(s1,"blue",s2,"green")
            plt.legend(['bruit','sans bruit'], loc=3) 

        else:
            ax.plot(s1, "blue", s2, "green", s3, "red")
            plt.legend(['sin','cos','sin+cos'], loc=3) 
    else :
        ax.plot(t,s1, "blue")

    if numero == 7:
        ax.set_xlim(-5,5)


    ax.set(xlabel='temps (s)',ylabel='tension (mV)',title= mytitle )

    fig.savefig("ex_"+str(numero)+".png")
    plt.show()
                        # Pas Te = 0.01s

t = num.arange(0.0, 8.0, 0.01)  #num.pi
# numpy.arange([start, ]stop, [step, ], dtype=None) -> numpy.ndarray

# Exos 1

# Data for plotting

#rand = random2.randint(3,9)
#rand2 = random2.randint(10,19)

s = num.random.normal(0,1,800)#200)

affichage('Exercice 1 : signal non-stationnaire',1,s)



# Exos 2

""" # Version 1
T = 3

N = 2

y = num.zeros(N)

x1 = num.linspace(-T, -T/2, N, endpoint=True)

x2 = num.linspace(-T/2, T/2, N, endpoint=True)

x3 = num.linspace(T/2, T, N, endpoint=True)

plt.plot(x1, y,"blue")

plt.plot(x2, y + 0.5,"blue")

plt.plot(x3, y,"blue")

plt.ylim([-0.5, 1])

plt.xlabel('temps (s)')
plt.ylabel('tension (mV)')
plt.title('Exercice 2 : signal Porte')
plt.grid()
plt.savefig("ex_2.png")

plt.show()
"""

# Version 2

def Draw_Door(T):

    x0 = -2*T # Pour décaler
    y0 = 0
    x0b = -T/2
    y0b = 0
    x1 = -T/2
    y1 = 1
    x2 = T/2
    y2 = 1
    x3 = T/2
    y3 = 0
    x3b = 2*T # Pour décaler
    y3b = 0

    x_values = [x0,x0b,x1,x2,x3,x3b]
    y_values = [y0,y0b,y1,y2,y3,y3b]

    plt.plot(x_values,y_values)

    #fig, plt = plt.subplots()

    plt.xlabel('temps (s)')
    plt.ylabel('tension (mV)')
    plt.title('Exercice 2 : signal Porte')
    plt.grid()
    plt.savefig("ex_2.png")

    plt.show()

large = input("Saisissez la largeur de la porte : ")
large = int(large)

Draw_Door(large)

# Exos 3

#s = num.random.normal(0,1,200)
s = num.exp(-t)

affichage('Exercice 3 : exponentielle décroissante',3,s)


# Exos 4

#s = num.random.normal(0,1,200)
no_bruit = 1 + 10 * num.sin(2 * num.pi * t)  
bruit = 1 + 10 * num.sin(2 * num.pi * t) + num.random.normal(0,1,800)#200)

affichage("Exercice 4 : Signal + Bruit",4,bruit,no_bruit)#,s2)

# Exos 5

sin = 3 * num.sin(2 * num.pi * t)
cos = 3 * num.cos(2 * num.pi * t)

sin_cos = sin + cos


affichage("Exercice 5 : sin, cos et sin+cos",5,sin,cos,sin_cos)

# Exos 6

# Définir la valeur "j" comme étant un complexe 

#j = num.complex(0,1) # 0 en a et 1 en "i"

signal = num.exp(1j*100*num.pi*t)

affichage("Exercice 6 : e^(j*100*pi*t)",6,signal)


# Exos 7 & 8

t = num.arange(-4.0, 4.0, 0.01)  #num.pi

Fe = 0.01
T = 1 / Fe

signal = num.exp(-1*abs(t))

fig,ax = plt.subplots()

plt.subplot(211)
plt.title("Exercice 7 : x(t) = e^(-a*abs(t))")
plt.plot(t,signal)

#affichage("Exercice 7 : x(t) = e^(-a*abs(t))",7,signal)

# inf = infinity
# num.inf borne non valide 
#X_signal = integrate.quad( function(1), -999, +999)


X_signal = num.fft.fft(signal)
n = signal.size
freq = num.fft.fftfreq(n, d = Fe)

# numpy.arange([start, ]stop, [step, ], dtype=None) -> numpy.ndarray


plt.subplot(212)
plt.plot(freq,abs(X_signal),"blue")

#plt.savefig("ex_8.png")

plt.title("Exercice 8 : Transformé de Fourier (TF) X(F) de x(t)")
plt.xlabel("Fréquence")
plt.ylabel("Amplitude")
plt.show()

#affichage("Exercice 8 : TF X(F) de x(t) ",8,X_signal)

fig.savefig("ex_7-8.png")



fig,ax = plt.subplots()

# Exos 9
t = num.arange(-T/2, T/2, 0.01)

def function(x):
    return num.exp(-1*abs(x))

def function2(n,t):
    return ( num.exp( -1*abs(t) )  * cos(n*(2*num.pi)/T) )


#A0 , err = integrate.quad(function, -T/2, T/2) 
#res, err = integrate.quad(function, -T/2, T/2)
#A0 = A0 * 1/T
#print('A0 : ', A0)

#for i in range(1,10):
#    print( str(integrate.quad( num.exp( -1*abs(t) )  * cos(n*(2*num.pi)/T) , -T/2, T/2)) )

#print(A)



# Exos 8 & 9 & 10

t = num.arange(-4.0, 4.0, 0.01)  #num.pi

Fe = 0.01
T = 1 / Fe

signal = num.exp(-1*abs(t))

plt.subplot(311)    # Exos 7
plt.title("x(t) = e^(-a*abs(t))")
plt.plot(t,signal)


X_signal = num.fft.fft(signal)
n = signal.size
freq = num.fft.fftfreq(n, d = Fe)

plt.subplot(312)    # Exos 8 & 9



plt.plot(freq,abs(X_signal),"blue",   freq,num.angle(X_signal),"red")
plt.legend(['Module X(F)','Angle'])

#plt.savefig("ex_8.png")    

plt.title("Transformé de Fourier (TF) X(F) de x(t)")
plt.xlabel("Fréquence")
plt.ylabel("Amplitude")
plt.title("Exercice 9 : Phase de la transfo")

plt.subplot(313)    # Exos 10
plt.plot(num.fft.fftshift(X_signal),"green")
#plt.legend(['TF Approximé','TF Inverse'])
plt.xlabel("Fréquence")
plt.ylabel("Amplitude")
plt.title("Exercice 10 : TF Approximé")

fig.savefig("ex_9-10.png")

plt.show()

fig,ax = plt.subplots()


plt.subplot(211)    # Exos 11
plt.plot(num.fft.ifft(X_signal),"blue")
plt.title("Exercice 11 : TF Inverse")

f0 = 5

signal_f0 = num.exp(-1*abs(t)) * num.exp(1j*2*num.pi*f0*t)

plt.subplot(212)
plt.plot(signal_f0,"green")
plt.title("Exercice 12 : TF en décalage fréquentiel (en f0= 5Hz)")

fig.savefig("ex_11-12.png")

plt.show()