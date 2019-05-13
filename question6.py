
from numpy import *
from numpy import random
import random

"""
Wouldn't trust the doctests because lots of changes were made afterwards. 
Just use a reference to give an idea of what the methods should do.
Will assume all instances of the class object have proper parameters (ie. instantiated properly).
"""

class Ship:
    """ A class of spaceships!"""
    
    def __init__(self, name, kind, laser, shield, hull_strength):
        """ (Ship, str, str, float, float, float) -> NoneType
        
        A Ship with a name, kind, laser power, shield strength, and hull strength.
        
        Kind can only be one of: Standard Spaceship, Warship, Speeder
        Must declare warships with Warship class.
        Must declar speeders with Speeder class.
        
        >>> myship = Ship('MyAwesomeShip', 'Standard Spaceship', 10., 50., 100.)
        >>> myship.name
        'MyAwesomeShip'
        >>> myship.kind
        'Standard Spaceship'
        >>> myship.laser
        10.
        >>> myship.shield
        50.
        >>> myship.hull_strength
        100.
        """
        self.name = name
        self.kind = kind #'Standard Spaceship'
        self.laser = laser
        self.shield = shield
        self.hull_strength = hull_strength
        
    def __str__(self):
        """ (Ship) -> str
        
        Return a string representation of my ship.
        
        >>> myship = Ship('MyAwesomeShip', 'Standard Spaceship', 10., 50., 100.)
        >>> str(myship)
        'MyAwesomeShip, kind: Standard Spaceship, laser: 10., shield: 50., hull strength: 100.'
        """
        
        return self.name + ', kind: ' + self.kind + ', laser: ' + str(self.laser) + ', shield: ' + str(self.shield) + ', hull strength ' + str(self.hull_strength)
        
    def status(self):
        """ (Ship) -> NoneType
        
        Print the current status of the ship, including laser power, shield status, hull status.
        
        >>> myship = Ship('MyAwesomeShip', 'Standard Spaceship', 10., 50., 100.)
        >>> myship.status()
        'Current Status of 'MyAwesomeShip': laser: 10., shield: 50., hull strength: 100.'
        """
        print('Current Status of {3}: laser: {0}, shield: {1}, hull strength: {2}'.format(self.laser, self.shield, self.hull_strength, self.name))
    
    def is_shot(self, other, other_laser):
        """ (Ship, Ship, int) -> NoneType
        
        'self' got shot by 'other' ship.
        
        >>> MyShip = Ship('Albert Einstein', 'Warship', 10., 50., 100.)
        >>> OtherShip = Ship('Niels Bohr', 'Standard Spaceship', 20., 30., 100.)
        >>> MyShip.is_shot(OtherShip)
        >>> status(MyShip)
        'Current Status of 'Albert Einstein': laser: 10., shield: 30., hull strength: 100.'
        """
        shield_life = self.shield - other_laser
        if (self.is_speeder() and (self.dodge() == True)):
            pass
        else:
            if shield_life >= 0:
                self.shield = shield_life
            else:
                self.shield = 0
                self.hull_strength += 0.5 * shield_life
                if self.hull_strength <= 0:
                    self.hull_strength = 0
                    print(self.name + ' is destroyed!')
            
    def shoot(self, other):
        """ (Ship, Ship) -> NoneType
        
        Shoot at another ship. Deal damage.
        
        >>> MyShip = Ship('Albert Einstein', 'Warship', 10., 50., 100.)
        >>> OtherShip = Ship('Niels Bohr', 'Standard Spaceship', 20., 30., 100.)
        >>> MyShip.shoot(OtherShip)
        >>> status(OtherShip)
        'Current Status of 'Albert Einstein': laser: 20., shield: 20., hull strength: 100.'
        """
        if self.is_warship():
            self.missile(other)
        else:
            other.is_shot(self, self.laser)
    
    def is_destroyed(self):
        """ (Ship) -> Bool
        Returns True if ship is destroyed (hull strength = 0), and False if not (hull strength > 0)
        
        >>> MyShip = Ship('Albert Einstein', 'Warship', 10., 0., 10.)
        >>> OtherShip = Ship('Niels Bohr', 'Standard Spaceship', 20., 30., 100.)
        >>> MyShip.is_destroyed()
        False
        >>> MyShip.is_shot(OtherShip)
        >>> status(MyShip)
        'Current Status of 'Albert Einstein': laser: 10., shield: 0., hull strength: 0.'
        >>> MyShip.is_destroyed()
        True 
        """
        if self.hull_strength <= 0:
            return True
        else:
            return False
        
    def is_warship(self):
        """ (Ship) -> bool
        Return True if Ship is a Warship.
        """
        return self.kind == 'Warship'
    
    def is_speeder(self):
        """ (Ship) -> bool
        Return True if Ship is a Speeder.
        """
        return self.kind == 'Speeder'
            
            
class Warship(Ship):
    """ 
    The Warship class!
    Special attributes: high powered missiles that fire 30% of the time with twice the amount of laser power.
    """
    def __init__(self, name, kind, laser, shield, hull_strength):
        self.kind = 'Warship'
        self.name = name
        self.laser = laser
        self.shield = shield
        self.hull_strength = hull_strength
        
    def missile(self, other):
        """ (Ship, Ship) -> NoneType
        
        Fire a high powered missile to 'other' with 2x laser power with a 30% chance.
        
        >>> MyShip = Ship('Albert Einstein', 'Warship', 10., 50., 100.)
        >>> OtherShip = Ship('Niels Bohr', 'Standard Spaceship', 20., 30., 100.)
        >>>
        >>> MyShip.missle(OtherShip)
        'Missile did not fire.'
        >>> status(OtherShip)
        'Current Status of 'Niels Bohr': laser: 20., shield: 30., hull strength: 100.'
        >>>
        >>> MyShip.missle(OtherShip)
        'Missile fired!'
        'Current Status of 'Niels Bohr': laser: 20., shield: 10., hull strength: 100.'
        """
        if (self.is_warship() and (random.uniform(0,1) < 0.33)):
            other.is_shot(self, 2 * self.laser)
            print('Missile fired by {0}!'.format(self.name))
        else:
            other.is_shot(self, self.laser)
            print('Missile did not fire.')

class Speeder(Ship):
    """
    The Speeder class!
    Special attributes: 50% chance of dodging incoming shots.
    """
    def __init__(self, name, kind, laser, shield, hull_strength):
        self.kind = 'Speeder'
        self.name = name
        self.laser = laser
        self.shield = shield
        self.hull_strength = hull_strength    
        
    def dodge(self):
        """ (Ship) -> Bool
        
        Dodges one incoming shot from 'other' with 50% chance.
        
        >>> OtherShip = Ship('Albert Einstein', 'Warship', 15., 40., 90.)
        >>> MyShip = Ship('Marie Curie', 'Speeder', 20., 30., 100.)
        >>>
        >>> MyShip.is_shot(OtherShip)
        >>> status(OtherShip)
        'Current Status of 'Albert Einstein': laser: 20., shield: 30., hull strength: 100.'
        >>>
        >>> MyShip.missle(OtherShip)
        'Missile fired!'
        'Current Status of 'Albert Einstein': laser: 20., shield: 10., hull strength: 100.'
        """
        if (self.is_speeder() and (random.uniform(0,1) < 0.5)):
            print('{0} successfully dodged the shot!'.format(self.name))
            return True
        else:
            return False
            

# Running the battleship simulation for 3 standard spaceships, 1 speeder and 1 warship with prescrbed stats
if __name__ == '__main__':
    ss = Speeder("Schroedinger", 'Speeder', 20., 20., 60.)
    w = Warship("Einstein", 'Warship', 25., 40., 100.)
    s1 = Ship("Bohr", 'Standard Spaceship',  20., 60., 100.)
    s2 = Ship("Rutherford", 'Standard Spaceship',  20., 60., 100.)
    s3 = Ship("Curie", 'Standard Spaceship',  20., 60., 100.)
    
    alive = [ss,w,s1,s2,s3]             # list of ships that are alive
    round = 0
    while len(alive) > 1:               # run while there are more than two ships alive
        s = random.choice(alive)        # randomly choose an attacker
        other = random.choice(alive)    # randomly choose an opponent
        if s != other:
            round +=1
            print("\nRound {0}:".format(round))
            print("{0} shot {1}!".format(s.name, other.name))
            s.shoot(other)
            s.status()          
            other.status()
            if other.is_destroyed():    # when a ship is destroyed, remove it from the alive list
                alive.remove(other)
    
    # Print the final victor
    print("\nThe final victor is {0}!!!".format((alive[0]).name))
            