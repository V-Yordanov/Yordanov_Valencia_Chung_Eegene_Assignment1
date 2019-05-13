
from numpy import *

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
        'Current Status: laser: 10., shield: 50., hull strength: 100.'
        """
        print('Current Status: laser: {0}, shield: {1}, hull strength: {2}'format(self.laser, self.shield, self.hull_strength))
    
    def is_shot(self, other):
        """ (Ship, Ship) -> NoneType
        
        'self' got shot by 'other' ship.
        
        >>> MyShip = Ship('Albert Einstein', 'Warship', 10., 50., 100.)
        >>> OtherShip = Ship('Niels Bohr', 'Standard Spaceship', 20., 30., 100.)
        >>> MyShip.is_shot(OtherShip)
        >>> status(MyShip)
        'Current Status: laser: 10., shield: 30., hull strength: 100.'
        """
        shield_life = self.shield - other.laser
        if shield_life >= 0:
            self.shield = shield_life
        else:
            self.shield = 0
            self.hull_strength -= 0.5 * shield_life
            
    def shoot(self, other):
        """ (Ship, Ship) -> NoneType
        
        Shoot at another ship. Deal damage.
        
        >>> MyShip = Ship('Albert Einstein', 'Warship', 10., 50., 100.)
        >>> OtherShip = Ship('Niels Bohr', 'Standard Spaceship', 20., 30., 100.)
        >>> MyShip.shoot(OtherShip)
        >>> status(OtherShip)
        'Current Status: laser: 20., shield: 20., hull strength: 100.'
        """
        other.is_shot(self)
    
    def is_destroyed(self):
        """ (Ship) -> Bool
        Returns True if ship is destroyed (hull strength = 0), and False if not (hull strength > 0)
        
        >>> MyShip = Ship('Albert Einstein', 'Warship', 10., 0., 10.)
        >>> OtherShip = Ship('Niels Bohr', 'Standard Spaceship', 20., 30., 100.)
        >>> MyShip.is_destroyed()
        False
        >>> MyShip.is_shot(OtherShip)
        >>> status(MyShip)
        'Current Status: laser: 10., shield: 0., hull strength: 0.'
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
    def is_warship(self):
        """ (Ship) -> bool
        Return True if Ship is a Warship.
        """
        return self.type == 'Warship'
        
    def missile(self, other):
        """ (Ship, Ship) -> NoneType
        Fire a high powered missile with 2x laser power with a 30% chance.
        >>> MyShip = Ship('Albert Einstein', 'Warship', 10., 50., 100.)
        >>> OtherShip = Ship('Niels Bohr', 'Standard Spaceship', 20., 30., 100.)
        >>> MyShip.missle(OtherShip)
        'Missile did not fire!'
        >>> status(OtherShip)
        'Current Status: laser: 20., shield: 30., hull strength: 100.'
        """

if __name__ == '__main__':
    
    s1 = Ship("Albert Einstein", 'Warship' 10., 50., 100.)
    s2 = Ship("Niels Bohr", 'Standard Spaceship',  20., 40., 100.)
    
    print(s1)
    print(s2)
        