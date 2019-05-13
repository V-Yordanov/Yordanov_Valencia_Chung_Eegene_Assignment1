#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 13 00:23:32 2019

Let's get some star wars/trek action going!

@author
"""
import random as random


class lethal_weapons:
    def __init__(vessel,spaceship,warship,speeder,full_strength):
        '''
        full_strength  = 100
        customize it into 100
        '''
        vessel.maximum = full_strength
    
    def hull_strength(vessel):
        vessel.lifeforce = vessel.maximum
        
    def shields_up(vessel):
        vessel.shield = vessel.maximum
        
    def laser_attack(vessel):
        hurt = 10
        if vessel.shield > hurt:
            vessel.shield -= hurt
        elif vessel.shield < hurt and vessel.shield > 0:
            diff = hurt - vessel.shield
            vessel.shield= 0 
            vessel.lifeforce -= (diff/2)
            
        else:
            vessel.lifeforce -= (hurt/2)
            
class warship(lethal_weapons):
    def __init__(vessel,full_strength,enhanced_offence):
        lethal_weapons.__init__(vessel,full_strength)
        vessel.extrapower = enhanced_offence
    def powerful_attack(vessel):
        vessel.laser_attack += vessel.extrapower

class speeder(lethal_weapons):
    def __init__(vessel,full_strength,dodge):
        lethal_weapons.__init__(vessel,full_strength)
        vessel.dodge = dodge

    def dodged_attack(vessel):
        chance = random.randint(1,101)
        if chance < 31:
           vessel.laser_attack = None
            
        
    
    

        
        
