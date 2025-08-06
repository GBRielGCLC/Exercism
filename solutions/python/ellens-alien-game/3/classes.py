"""Solution to Ellen's Alien Game exercise."""


class Alien():
    """Create an Alien object with location x_coordinate and y_coordinate.

    Attributes
    ----------
    (class)total_aliens_created: int
    x_coordinate: int - Position on the x-axis.
    y_coordinate: int - Position on the y-axis.
    health: int - Number of health points.

    Methods
    -------
    hit(): Decrement Alien health by one point.
    is_alive(): Return a boolean for if Alien is alive (if health is > 0).
    teleport(new_x_coordinate, new_y_coordinate): Move Alien object to new coordinates.
    collision_detection(other): Implementation TBD.
    """
    total_aliens_created = 0

    def __init__(self, x_coordinate=0, y_coordinate=0):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate

        self.health = 3

        Alien.total_aliens_created += 1

    def hit(self):
        self.health -= 1

    def is_alive(self):
        return self.health > 0

    def teleport(self, x_coordinate, y_coordinate):
        if (not isinstance(x_coordinate, int)) or (not isinstance(y_coordinate, int)):
            raise TypeError("Invalid coordinates, please use integers.")

        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate

    def collision_detection(self, other):
        if (other.x_coordinate == self.x_coordinate) and (other.y_coordinate == self.y_coordinate):
            return True

        return None

def new_aliens_collection(alien_start_positions):
    aliens = []

    for x_coordinate, y_coordinate in alien_start_positions:
        aliens.append(Alien(x_coordinate, y_coordinate))

    return aliens

alien = Alien(1, 0)
alien = Alien(2, 0)

print(Alien.total_aliens_created)

#TODO:  create the new_aliens_collection() function below to call your Alien class with a list of coordinates.
