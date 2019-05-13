# CTA200H Question 3

import numpy as np
import pylab as plt
import scipy as sc
import matplotlib.pyplot as py
from time import time
from scipy import special

# Question 3 (a)

def fm(theta, m, x):
    """
    Integrad in bessel function Jm(x).
    """
    return np.cos((m*theta) - x*np.sin(theta))/np.pi

def simpson_integration(f, N, a, b, m, x):
    """
    Simpson method of integration.
    f is the integrand being integrated
    N is the number of sections in interval
    a is the start of the interval
    b is the end of the interval
    m is a nonnegative integer needed for integrand of bessel function
    """
    h = (b-a)/N #width of the quadratic curves
    #implimenting simpson rule equation
    t1 = f(a, m, x) + f(b, m, x) #setting inital sum value
    t2 = 0
    #looping through odd terms of sum
    for k in range(1,N,2):
        t2 += f(a + k*h, m, x)
    t2  *= 4

    t3 = 0
    for k in range(2,N,2):
        t3 += f(a + k*h, m, x)
    t3 *= 2

    #multiplying total sum
    t = (h/3) * (t1 + t2 + t3)

    #print("Integral from simpson's rule = ", t)
    return t

def J(m, x):
    """
    Bessel function Jm(x).
    m is a nonnegative int
    x >= 0
    """
    N = 1000 #number of sections splitting interval
    a = 0 #start of interval
    b = np.pi #end of interval
    
    s = simpson_integration(fm, N, a, b, m, x)
    
    return s


x = np.linspace(0, 20, 100)
#running bessel function for m=0,1,2
y_0 = J(0, x)
y_1 = J(1, x)
y_2 = J(2, x)
y_3 = J(3, x)

plt.figure(figsize=(10,6))
#ploting bessel function for m =0,1,2
plt.plot(x, y_0, label='simpson: m=0', marker='.', linestyle='none', color='b')
plt.plot(x, y_1, label='simpson: m=1', marker='.', linestyle='none', color='orange')
plt.plot(x, y_2, label='simpson: m=2', marker='.', linestyle='none', color='g')
plt.plot(x, y_3, label='simpson: m=3', marker='.', linestyle='none', color='r')

# using scipy's special.jv function to find y values and compare them to
# Simpson's method for m=0,1,2, 3
y_sc0 = sc.special.jv(0, x)
y_sc1 = sc.special.jv(1, x)
y_sc2 = sc.special.jv(2, x)
y_sc3 = sc.special.jv(3, x)

#plotting the results from scipy's function overtop our own results
plt.plot(x, y_sc0, label='scipy: m=0', color='b')
plt.plot(x, y_sc1, label='scipy: m=1', color='orange')
plt.plot(x, y_sc2, label='scipy: m=2', color='g')
plt.plot(x, y_sc3, label='scipy: m=3', color='r')

plt.legend()
plt.xlabel("x")
plt.ylabel("Jm(x)")
plt.title("Bessel Function for Different m Values:\nSimpson's vs. Scipy Method")
plt.show()
plt.clf()

#==============================================================================

# Question 3 b

def I(I_0, lamb, r):
    """
    Intensity pattern from the telescope.
    I_0     intensity at the centre
    lamb    wavelength of light
    r       is defined to be equal to aq/R
    """
    x = 2*np.pi*r / lamb  
#    return I_0 * (2*J(1,x)/x)**2
    return I_0 * (2*sc.special.jv(1, x)/x)**2


I_0 = 1
lamb = 0.5 #in µm

x = np.arange(-1, 1, 0.01)
y = np.arange(-1, 1, 0.01)
xx, yy = np.meshgrid(x, y)
r = np.sqrt(xx**2 + yy**2)
z = I(I_0, lamb, r)

plt.figure(figsize=(6,6))
plt.imshow(z, extent=[-1,1,-1,1])
plt.title("Intensity Pattern (Normal)\nwith I_0 = {0}, $\lambda$ = {1}µm".format(I_0,lamb))
plt.xlabel("x in µm")
plt.ylabel("y in µm")
plt.show()
plt.clf()

plt.figure(figsize=(6,6))
plt.imshow(z, vmin = 0, vmax = 0.1, extent=[-1,1,-1,1])
plt.title("Intensity Pattern (High Contrast vmax = 0.1)\nwith I_0 = {0}, $\lambda$ = {1}µm".format(I_0,lamb))
plt.xlabel("x in µm")
plt.ylabel("y in µm")
plt.show()
plt.clf()


#==============================================================================

# Question 3 c

from scipy import ndimage
from scipy import signal, misc

# Import some image data
from skimage import data
camera = data.camera()

# Define grid
x1 = np.linspace(-1.5, 1.5, 512)
y1 = np.linspace(-1.5, 1.5, 512)
[X,Y] = np.meshgrid(x1,y1)
r1 = np.sqrt(X**2 + Y**2)

v_I = np.vectorize(I) # Vectorize point spread function
z1 = v_I(I_0, 0.2, r1)

# Convolution
conv = signal.fftconvolve(camera,z1) # other methods took indefinite time

# Plotting original image
plt.figure(0)
plt.imshow(camera)
plt.title("Original Image")
plt.show()

# Plotting convolved image
plt.figure(1)
plt.imshow(conv)
plt.title("Convolved Image")
plt.xlim(200,800)
plt.ylim(800,200)
plt.show()


