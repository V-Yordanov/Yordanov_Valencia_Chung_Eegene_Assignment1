"""
Types:
- Standard Spaceships
- Warships
- Speeders

Each has:
- Lasers
- Shields
- Hull Strength
- Name

Warships:
- high powered missiles which fires 30% of the time

Speeders:
- 50% chance of dodging incoming shots

When a spaceship is shot by another ship:
1) depletes its shields equal to the strength of the shot
2) when it runs out of shields, it takes hull damage at 50% of the shot strength
3) once hull is breached, the ship is destroyed

class Ship which defines standard spaceship
two classes which inherit from Ship called Warship and Speeder
the classes should store the ship's shield strength, hull strength, laser power, and name
methods: ship shoots, is shot at, ship destroyed (or not), print a diagnostic summary of ship's status

instantiate 3 regular ships, 1 warship, 1 speeder
the spaceships shoot randomly at each other until only one remains
print a long of the battles as it progresses
declare a final victor

"""
from numpy import *

class Ship:
    """ A class of spaceships!"""
    
    def __init__(self, name, laser, shield, hull_strength):
        """ (Ship, str, float, float, float) -> NoneType
        
        A Ship with a name, laser power, shield strength, and hull strength.
        
        >>> myship = Ship('MyAwesomeShip', 10., 50., 100.)
        >>> myship.name
        'MyAwesomeShip'
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
        
        >>> myship = Ship('MyAwesomeShip', 10., 50., 100.)
        >>> str(myship)
        'MyAwesomeShip, laser: 10., shield: 50., hull strength: 100.'
        """
        
        return self.name + ', laser: ' + str(self.laser) + ', shield: ' + str(self.shield) + ', hull strength ' + str(self.hull_strength)
        

if __name__ == '__main__':
    
    s1 = Ship("Albert Einstein", 10., 50., 100.)
    s2 = Ship("Niels Bohr", 20., 40., 100.)
    
    print(s1)
    print(s2)
        