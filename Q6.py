
from numpy import *
from numpy import random
import random

class Ship:
    """ A class of spaceships!"""
    
    def __init__(self, name, type, laser, shield, hull_strength):
        """ (Ship, str, str, float, float, float) -> NoneType
        
        A Ship with a name, type, laser power, shield strength, and hull strength.
        
        Type can only be one of: Standard Spaceship, Warship, Speeder
        
        >>> myship = Ship('MyAwesomeShip', 'Standard Spaceship', 10., 50., 100.)
        >>> myship.name
        'MyAwesomeShip'
        >>> myship.type
        'Standard Spaceship'
        >>> myship.laser
        10.
        >>> myship.shield
        50.
        >>> myship.hull_strength
        100.
        """
        self.name = name
        if self.type == 'Warship':
            self = Warship(self)
        elif self.type == 'Speeder':
            self = Speeder(self)
        else:
            self.type = "Standard Spaceship"
            self.laser = laser
            self.shield = shield
            self.hull_strength = hull_strength
        
    def __str__(self):
        """ (Ship) -> str
        
        Return a string representation of my ship.
        
        >>> myship = Ship('MyAwesomeShip', 'Standard Spaceship', 10., 50., 100.)
        >>> str(myship)
        'MyAwesomeShip, type: Standard Spaceship, laser: 10., shield: 50., hull strength: 100.'
        """
        
        return self.name + ', type: ' + self.type + ', laser: ' + str(self.laser) + ', shield: ' + str(self.shield) + ', hull strength ' + str(self.hull_strength)
        
    def status(self):
        """ (Ship) -> NoneType
        
        Print the current status of the ship, including laser power, shield status, hull status.
        
        >>> myship = Ship('MyAwesomeShip', 'Standard Spaceship', 10., 50., 100.)
        >>> myship.status()
        'Current Status of 'MyAwesomeShip': laser: 10., shield: 50., hull strength: 100.'
        """
        print('Current Status of {3}: laser: {0}, shield: {1}, hull strength: {2}'format(self.laser, self.shield, self.hull_strength, self.name)
    
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
        if self.is_speeder():
            self.dodge()
        else:
            if shield_life >= 0:
                self.shield = shield_life
            else:
                self.shield = 0
                self.hull_strength -= 0.5 * shield_life
                if self.hull_strength <= 0:
                    self.hull_stregnth = 0
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
            self.missile()
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
            
            
class Warship(Ship):
    """ 
    The Warship class!
    Special attributes: high powered missiles that fire 30% of the time with twice the amount of laser power.
    """
    def __init__(self):
        self.type = 'Warship'
        self.name = name
        self.laser = laser
        self.shield = shield
        self.hull_strength = hull_strength
        
    def is_warship(self):
        """ (Ship) -> bool
        Return True if Ship is a Warship.
        """
        return self.type == 'Warship'
        
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
        if (self.is_warship() and (random.uniform() < 0.3)):
            other.is_shot(self, 2 * self.laser)
            print('Missile fired!')
        else:
            other.is_shot(self, self.laser)
            print('Missile did not fire.')

class Speeder(Ship):
    """
    The Speeder class!
    Special attributes: 50% chance of dodging incoming shots.
    """
    def __init__(self):
        self.type = 'Speeder'
        self.name = name
        self.laser = laser
        self.shield = shield
        self.hull_strength = hull_strength    
        
    def is_speeder(self):
        """ (Ship) -> bool
        Return True if Ship is a Speeder.
        """
        return self.type == 'Speeder'
        
    def dodge(self):
        """ (Ship, Ship) -> NoneType
        
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
        if (self.is_speeder() and (random.uniform() < 0.5)):
            print('Successfully dodged the shot!')
        else:
            if shield_life >= 0:
                self.shield = shield_life
            else:
                self.shield = 0
                self.hull_strength -= 0.5 * shield_life
            
            print('Missile did not fire.')

        

if __name__ == '__main__':
    ss = Ship("Schroedinger", 'Speeder', 20., 30., 100.)
    w = Ship("Einstein", 'Warship', 15., 40., 90.)
    s1 = Ship("Bohr", 'Standard Spaceship',  20., 60., 100.)
    s2 = Ship("Rutherford", 'Standard Spaceship',  20., 60., 100.)
    s3 = Ship("Curie", 'Standard Spaceship',  20., 60., 100.)
    
    alive = [ss,w,s1,s2,s3]
    while len(alive) > 1
        for s in alive:
            other = random.choice(ships)
            if s != other:
                s.shoot(other)
                s.status()
                other.status()
                if other.is_destroyed():
                    alive.remove(other)
    print("The final victor is {0}!!!".format(str(alive[0])))
            