"""
author: Valencia Yordanov
"""
from math import *
import numpy as np
import time as time
import random as random


def binomialCoeff(n,k):    
    '''
    This function takes two values, n and k, and calculates their binomial
    coefficient
    '''  
    #Initializing all variables and arrays 
    delete_slice = k-n
    i=0
    j=0    
    numerator = 1
    denominator = 1   
    a = np.arange(n+1,dtype='int64')
    a = np.delete(a,0)
    a = a[delete_slice:] #This is to cancel out some of the factorial terms
    c_size = n-k 
    c = np.arange(c_size+1,dtype='int64')
    c = np.delete(c,0)

    
    #These for loops and if statements are responsible for calculating the 
    #factorials. I Calculate the numerator and denominator terms separately
    if n==k:
        numerator = 1   
    else:
        for i in a:
            numerator = numerator*i       
    for j in c:
        denominator = denominator*j
        
    #Calculating the denominator by multiplying the denominator factors above
    #then dividing the numerator by the denominator to give the binomial coeff
    denominator = denominator
    binomial_coefficient = numerator//denominator
    
    return binomial_coefficient




#Now to write the first 20 lines of pascals triangle. The binomial coefficient
#function can help because n is the line number starting at the zeroth line,
#and k is the number of the entry in the line. k <= n+1
def line_generator(n):
    '''
    This function creates the given line of pascals triangle. For this part of
    the question, the line number is the same thing as n, in the binomial
    coefficient formula
    '''
    #initializing variables and lists
    i = 0
    k = n+1
    line_elements = []
    
    #This for loop calculates each element of the line and appends its value to
    #a list
    for i in range(k):
        entry = binomialCoeff(n,i)
        line_elements.append(entry)

    return line_elements
    


def pascals_triangle(num_lines):
    '''
    Now that we have our functions, let's print out the first 20 lines of
    Pascal's triangle
    
    This function print x amount of lines in Pascal's triangle
    '''
    for i in range(num_lines):
        print(line_generator(i))




def coin_prob(n,k,p):
    '''
    This is the coin probability function, using the binomial coefficient fn
    
    Here we are physically flipping the coin n times, and hoping to get heads
    k times
    '''
    prob = binomialCoeff(n,k)*(p**(k))*(1-p)**(n-k)
    return prob


#The print below is telling me that the probability of any of the combinations
#below totals to 1. As expected
#print(coin_prob(4,0,0.5)+coin_prob(4,1,0.5)+coin_prob(4,2,0.5)+coin_prob(4,3,0.5)+coin_prob(4,4,0.5))
print('The probability of the batter hitting the ball once in four tries is', coin_prob(4,1,0.25))


#Here we are simulating, a baseball player with p = 0.25. We will use a random
#number generator to obtain a number between 0 and 1. If the number is less
#than 0.25, it will be recorded as a hit, if it is greater it is a miss

def hit_or_miss(N):
    hits = 0
    misses = 0
    for i in range(N):
        hit_miss = random.random()
        if hit_miss >= 0.25:
            misses += 1
        elif hit_miss <= 0.25:
            hits += 1
        else:
            print('Something wrong happened')
    return hits,misses






