# 6.00x Problem Set 7: Simulating robots

import math
import random

import ps7_visualize
#from ps7_visualize import *
import pylab

# For Python 2.7:
from ps7_verify_movement27 import *

# If you get a "Bad magic number" ImportError, comment out what's above and
# uncomment this line (for Python 2.6):
# from ps7_verify_movement26 import testRobotMovement


# === Provided class Position
class Position(object):
    """
    A Position represents a location in a two-dimensional room.
    """
    def __init__(self, x, y):
        """
        Initializes a position with coordinates (x, y).
        """
        self.x = x
        self.y = y
        
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def getNewPosition(self, angle, speed):
        """
        Computes and returns the new Position after a single clock-tick has
        passed, with this object as the current position, and with the
        specified angle and speed.

        Does NOT test whether the returned position fits inside the room.

        angle: number representing angle in degrees, 0 <= angle < 360
        speed: positive float representing speed

        Returns: a Position object representing the new position.
        """
        old_x, old_y = self.getX(), self.getY()
        angle = float(angle)
        # Compute the change in position
        delta_y = speed * math.cos(math.radians(angle))
        delta_x = speed * math.sin(math.radians(angle))
        # Add that to the existing position
        new_x = old_x + delta_x
        new_y = old_y + delta_y
        return Position(new_x, new_y)

    def __str__(self):  
        return "(%0.2f, %0.2f)" % (self.x, self.y)


# === Problem 1
class RectangularRoom(object):
    """
    A RectangularRoom represents a rectangular region containing clean or dirty
    tiles.

    A room has a width and a height and contains (width * height) tiles. At any
    particular time, each of these tiles is either clean or dirty.
    """
    def __init__(self, width, height):
        """
        Initializes a rectangular room with the specified width and height.

        Initially, no tiles in the room have been cleaned.

        width: an integer > 0
        height: an integer > 0
        """
        self.width       = width
        self.height      = height
        self.cleaned_tiles = []
    
    def cleanTileAtPosition(self, pos):
        """
        Mark the tile under the position POS as cleaned.

        Assumes that POS represents a valid position inside this room.

        pos: a Position
        """
        x = math.floor(pos.getX())
        y = math.floor(pos.getY())
        
        if (x,y) not in self.cleaned_tiles:
            self.cleaned_tiles.append((x,y)) 

    def isTileCleaned(self, m, n):
        """
        Return True if the tile (m, n) has been cleaned.

        Assumes that (m, n) represents a valid tile inside the room.

        m: an integer
        n: an integer
        returns: True if (m, n) is cleaned, False otherwise
        """
        return (m,n) in self.cleaned_tiles
    
    def getNumTiles(self):
        """
        Return the total number of tiles in the room.

        returns: an integer
        """
        return self.width * self.height

    def getNumCleanedTiles(self):
        """
        Return the total number of clean tiles in the room.

        returns: an integer
        """
#        return len(self.cleaned_tiles)
        cleanTiles = 0
        for i in range(self.width):
            for j in range(self.height):
                if self.isTileCleaned(i, j):
                    cleanTiles += 1
        return cleanTiles

    def getRandomPosition(self):
        """
        Return a random position inside the room.

        returns: a Position object.
        """
#        x = random.choice(range(self.width))
#        y = random.choice(range(self.height))
#        
#        pos = Position(x,y)
#        return pos
        return Position(random.randint(0,self.width-1), random.randint(0,self.height-1))

    def isPositionInRoom(self, pos):
        """
        Return True if pos is inside the room.

        pos: a Position object.
        returns: True if pos is in the room, False otherwise.
        """
#        return (0 <= pos.getX() < self.width) and (0 <= pos.getY < self.height)
        if (0 <= pos.getX() < self.width) and (0 <= pos.getY() < self.height):
            return True
        else:
            return False


class Robot(object):
    """
    Represents a robot cleaning a particular room.

    At all times the robot has a particular position and direction in the room.
    The robot also has a fixed speed.

    Subclasses of Robot should provide movement strategies by implementing
    updatePositionAndClean(), which simulates a single time-step.
    """
    def __init__(self, room, speed):
        """
        Initializes a Robot with the given speed in the specified room. The
        robot initially has a random direction and a random position in the
        room. The robot cleans the tile it is on.

        room:  a RectangularRoom object.
        speed: a float (speed > 0)
        """
        self.room      = room
        self.direction = int(360 * random.random()) 
        self.pos       = self.room.getRandomPosition()#Position(room.width * random.random(), room.height * random.random())
        self.room.cleanTileAtPosition(self.pos)
        if speed > 0:
            self.speed = speed
        else:
            raise ValueError('Speed input must be greater than zero(0)')
#        self.pos       = getNewPosition(self.direction, self.speed)
        
    def getRobotPosition(self):
        """
        Return the position of the robot.

        returns: a Position object giving the robot's position.
        """
        return self.pos
    
    def getRobotDirection(self):
        """
        Return the direction of the robot.

        returns: an integer d giving the direction of the robot as an angle in
        degrees, 0 <= d < 360.
        """
        return self.direction

    def setRobotPosition(self, position):
        """
        Set the position of the robot to POSITION.

        position: a Position object.
        """
        if self.room.isPositionInRoom(position):
            self.pos = position
        else:
            raise ValueError('Position input is not in the room')

    def setRobotDirection(self, direction):
        """
        Set the direction of the robot to DIRECTION.

        direction: integer representing an angle in degrees
        """
        self.direction = direction

    def updatePositionAndClean(self):
        """
        Simulate the raise passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        raise NotImplementedError # don't change this!


# === Problem 2
class StandardRobot(Robot):
    """
    A StandardRobot is a Robot with the standard movement strategy.

    At each time-step, a StandardRobot attempts to move in its current
    direction; when it would hit a wall, it *instead* chooses a new direction
    randomly.
    """
    def updatePositionAndClean(self):
        """
        Simulate the raise passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        new_pos = self.pos.getNewPosition(self.direction, self.speed)
        if self.room.isPositionInRoom(new_pos):
            self.setRobotPosition(new_pos)
            self.room.cleanTileAtPosition(self.pos)
        else:
            self.setRobotDirection(int(360 * random.random()))
            self.updatePositionAndClean()
# Uncomment this line to see your implementation of StandardRobot in action!
##testRobotMovement(StandardRobot, RectangularRoom)


# === Problem 3
def runSimulation(num_robots, speed, width, height, min_coverage, num_trials,
                  robot_type):
    """
    Runs NUM_TRIALS trials of the simulation and returns the mean number of
    time-steps needed to clean the fraction MIN_COVERAGE of the room.

    The simulation is run with NUM_ROBOTS robots of type ROBOT_TYPE, each with
    speed SPEED, in a room of dimensions WIDTH x HEIGHT.

    num_robots: an int (num_robots > 0)
    speed: a float (speed > 0)
    width: an int (width > 0)
    height: an int (height > 0)
    min_coverage: a float (0 <= min_coverage <= 1.0)
    num_trials: an int (num_trials > 0)
    robot_type: class of robot to be instantiated (e.g. StandardRobot or
                RandomWalkRobot)
    """
    mean_time_taken = 0
    robots           = []
    
    for num in range(num_trials):
        '''optional visualization'''
        anim = ps7_visualize.RobotVisualization(num_robots, width, height)
        
        room = RectangularRoom(width, height)
        for robot in xrange(num_robots):
            robots.append(robot_type(room, speed))
        
        while room.getNumCleanedTiles() < (min_coverage * room.getNumTiles()):
            for robot in robots:
                robot.updatePositionAndClean()
            mean_time_taken += 1
            anim.update(room, robots)
        anim.done()
    return float(mean_time_taken/ num_trials)
            
runSimulation(10, 1.0, 30, 30, 0.8, 10, StandardRobot)


# === Problem 4
class RandomWalkRobot(Robot):
    """
    A RandomWalkRobot is a robot with the "random walk" movement strategy: it
    chooses a new direction at random at the end of each time-step.
    """
    def updatePositionAndClean(self):
        """
        Simulate the passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        new_pos = self.pos.getNewPosition(self.direction, self.speed)
        if self.room.isPositionInRoom(new_pos):
            self.setRobotPosition(new_pos)
            self.room.cleanTileAtPosition(self.pos)
            self.setRobotDirection(int(360 * random.random()))
        else:
            self.setRobotDirection(int(360 * random.random()))
            self.updatePositionAndClean()

#runSimulation(10, 1.0, 15, 20, 0.8, 30, RandomWalkRobot)

def showPlot1(title, x_label, y_label):
    """
    What information does the plot produced by this function tell you?
    """
    num_robot_range = range(1, 11)
    times1 = []
    times2 = []
    for num_robots in num_robot_range:
        print "Plotting", num_robots, "robots..."
        times1.append(runSimulation(num_robots, 1.0, 2, 2, 0.8, 10, StandardRobot))
        times2.append(runSimulation(num_robots, 1.0, 2, 2, 0.8, 10, RandomWalkRobot))
    pylab.plot(num_robot_range, times1)
    pylab.plot(num_robot_range, times2)
    pylab.title(title)
    pylab.legend(('StandardRobot', 'RandomWalkRobot'))
    pylab.xlabel(x_label)
    pylab.ylabel(y_label)
    pylab.show()

    
def showPlot2(title, x_label, y_label):
    """
    What information does the plot produced by this function tell you?
    """
    aspect_ratios = []
    times1 = []
    times2 = []
    for width in [10, 20, 25, 10]:
        height = 300/width
        print "Plotting cleaning time for a room of width:", width, "by height:", height
        aspect_ratios.append(float(width) / height)
        times1.append(runSimulation(2, 1.0, width, height, 0.8, 200, StandardRobot))
        times2.append(runSimulation(2, 1.0, width, height, 0.8, 200, RandomWalkRobot))
    pylab.plot(aspect_ratios, times1)
    pylab.plot(aspect_ratios, times2)
    pylab.title(title)
    pylab.legend(('StandardRobot', 'RandomWalkRobot'))
    pylab.xlabel(x_label)
    pylab.ylabel(y_label)
    pylab.show()
    

# === Problem 5
#
# 1) Write a function call to showPlot1 that generates an appropriately-labeled
#     plot.
#
#       (... your call here ...)
#
#showPlot1("Plotting number robots...", 'x', 'y')
#showPlot2("Plotting number robots...", 'x', 'y')
#
# 2) Write a function call to showPlot2 that generates an appropriately-labeled
#     plot.
#
#       (... your call here ...)
#
