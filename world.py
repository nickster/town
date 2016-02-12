#!/usr/bin/python

import pdb
import datetime

"""
Just finished:
Agents now calculate commute time based on distance and leave at different times, but all arrive at same time.

Todo:
Make assigning a job to an agent as simple as calling the Occupations object, which has pre-sets for occupations.
Commute home
Plan ahead time it takes to get home
Two "forces" & priorities is a combination of what they spur
Farm with economic output
spacial awareness & basic social interaction
immutable and mutable agent traits, moods
personalities change over time
choice & behavior based on traits, moods, randomness (ongoing tasks, spacial, new)
hierarchy of needs
memory & fact communication
Show visually - "N-m" on grid
Random darkness: Sickness and death, depression, alcoholism, drugs, violence, crime
NLP-driven feelings for real-world events. Search "hit by a car" and "feelings".

Issues
Remove need to pass agent to a child Action class

"""

class Agent(object):
    'Base class for all agents. Creates an agent including where they start and gives them a set of priorities, with their job at the top of the list.
    
    def __init__(self, name, point, world):
        self.name = name
        self.location = point
        self.home = Home(point)
        self.priorities = []
        self.priorities.append(Job(self, Point(4,4),8))
        world.agents.append(self)
    
    def action(self):
        #iterate through priorities and .do 'em
        for activity in self.priorities:
            activity.do()
            if activity.state == "completed":
                self.priorities.remove(activity)

class Home(object):
    'The home object of an agent. Currently used just for a location, but in the future can have properties.'
    
    def __init__(self, point):
        self.location = point

class Job(object):
    'The primary occupation of an agent. Currently takes '
    
    def __init__(self, agent, point, starthour):
        self.agent = agent
        self.state = None
        self.location = point
        self.starthour = self.setcommutetime(datetime.timedelta(hours=starthour))
    
    def setcommutetime(self, starthour):
        moves = abs(self.agent.home.location.x - self.location.x) + abs(self.agent.home.location.y - self.location.y)
        totalcommutetime = moves * time.increment
        return (starthour - totalcommutetime)
        
        #calculate time to leave
        #set leave time in job.do schedule
        
    def do(self):
        delta = time.moment - self.starthour
        if delta.hour == 0 and delta.minute == 0:
            self.agent.priorities.append(MoveTo(self.agent, self.location))
        else:
            pass
        
class Actions(object):
    def __init__(self, agent):
        self.agent = agent
        self.state = None

class MoveTo(Actions):
    def __init__(self, agent, point):
        self.point = point
        self.agent = agent
        self.state = None
       
    def moveone(self, direction):
        if direction == "up":
            self.agent.location.y = self.agent.location.y + 1
            print self.agent.name + " moved " + direction
        elif direction == "down":
            self.agent.location.y = self.agent.location.y - 1
            print self.agent.name + " moved " + direction
        elif direction == "left":
            self.agent.location.x = self.agent.location.x - 1 
            print self.agent.name + " moved " + direction 
        elif direction == "right":
            self.agent.location.x = self.agent.location.x + 1
            print self.agent.name + " moved " + direction
        
    def do(self):
        if self.agent.location.x - self.point.x > 0:
            self.moveone("left")
        elif self.agent.location.x - self.point.x < 0:
            self.moveone("right")
            pdb.set_trace
        elif self.agent.location.y - self.point.y > 0:
            self.moveone("down")
        elif self.agent.location.y - self.point.y < 0:
            self.moveone("up")
        if str(self.point) != str(self.agent.location):
            self.state = "in progress"
        else: 
            self.state = "completed"
            
        
class World(object):
    #A living breathing world where agents can be appended to points
    def __init__(self, size):
        self.agents = []
        self.x = range(0,size)
        self.y = range(0,size)
        for i in self.x:
              i = []
        for i in self.y:
              i = []

class Time(object):
    #The hand of everything
    def __init__(self):
        self.moment = datetime.datetime(year=2015,month=5,day=25,hour=0)
        self.increment = datetime.timedelta(minutes=15)
        
class Point(object):
  def __init__(self, x, y):
    self.x, self.y = x, y

  def __str__(self):
    return "{}, {}".format(self.x, self.y)

  def __neg__(self):
    return Point(-self.x, -self.y)

  def __add__(self, point):
    return Point(self.x+point.x, self.y+point.y)

  def __sub__(self, point):
    return self + -point
   
world = World(50)
time = Time()
nick = Agent("Nick", Point(5,5), world)
john = Agent("John", Point(7,2), world)
burke = Agent("Burke", Point(1,9), world)
print time.moment

while time.moment.day < 26:
    print "It's " + str(time.moment.hour) + ":" + str(time.moment.minute)
    for agent in world.agents:
        agent.action()
    time.moment = time.moment + time.increment
        
