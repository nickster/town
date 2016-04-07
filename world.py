#!/usr/bin/python

import pdb
import time
import datetime
import random
import agent
import occupations
import priorities
import point
                
def doPriorities(priorities):
    for object in priorities:
        if hasattr(object, "do"):
            object.do()
        if hasattr(object, "priorities"):
            if len(object.priorities) > 0:
                doPriorities(object.priorities)

def agents_at_point(x, y):
    near = []
    for agent in x:
        if y.__contains__(agent):
            near.append(agent)
    return near

class Family(object):
    'Creates a family priority tailored to an agent, and that agents family property points to that family object as well. On init, creates a spouse and two children with occupations, and creates a new, unique family object for each of them but does not then create a new family (only if its a family head). Every family object has a list of family members and points to the agent objects.'
    
    def __init__(self, agent):
        self.agent = agent
        self.home = agent.location
        self.priorities = []
        self.priorities.append("Family dinner")
        self.siblings = []
        self.children = []
        self.spouse = []
        self.parents = []
        if self.agent.kind == "Seed":
            self.create_spouse()
            self.have_children()
        add_to_world(self.agent)
            
    def have_children(self):
        total = random.choice(range(0,5))
        while total > 0:
            gender = random.choice(["male","female"])
            if gender == "male":
                name_set = boys_names
            else:
                name_set = girls_names
            home = point.Point(self.agent.home.x, self.agent.home.y)
            new_child = agent.Agent(random.choice(name_set), gender, "Sprout", home, "Student", world)
            self.children.append(new_child)
            self.spouse.family.children.append(new_child)
            new_sibling_index = len(self.children) - 1 
            new_child.family.parents.append(self.agent)
            new_child.family.parents.append(self.spouse)
            for child in self.children:
                child.family.siblings.append(new_child)
            total = total - 1
            
    def create_spouse(self):
        home = point.Point(self.agent.home.x, self.agent.home.y)
        if self.agent.gender == "male":
            gender = "female"
            name_set = girls_names
        else:
            gender = "male"
            name_set = boys_names
        self.spouse = agent.Agent(random.choice(name_set), gender, "Sprout", home, "Farmer", world)
        self.spouse.family.spouse = self.agent
        
    def do(self):
        pass
    
def remove_from_world(agent):
    world.x[agent.location.x].remove(agent)
    world.y[agent.location.y].remove(agent)
    
def add_to_world(agent):
    world.x[agent.location.x].append(agent)
    world.y[agent.location.y].append(agent)


class Move(object):
    def __init__(self, agent):
        self.agent = agent
        pass
       
    def move_one(self, direction):
        remove_from_world(self.agent)
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
        add_to_world(self.agent)
        
    def move_toward(self, point):
        print agent.name + " is beginning to move towards " + str(point)
        point = point
        if self.agent.location.x - point.x > 0:
            self.move_one("left")
        elif self.agent.location.x - point.x < 0:
            self.move_one("right")
        elif self.agent.location.y - point.y > 0:
            self.move_one("down")
        elif self.agent.location.y - point.y < 0:
            self.move_one("up")
        
class World(object):
    #A living breathing world where agents can be appended to points
    def __init__(self, size):
        self.agents = []
        self.x = range(0,size)
        self.y = range(0,size)
        for i in self.x:
              self.x[i] = []
        for i in self.y:
              self.y[i] = []
   
world = World(50)
boys_names = ["Crane","Hicks","Gordon","Allum","Chais","Bamtug","Reed-meed","Hillbilly","Simon Says","A.B.S","Chicago"]
girls_names = ["Mara","Kyra","Kristee", "Noor","Gia","Gwen","Bertha", "Charlene","Quizza","Maya-Angelou","Emily Dickinson"]
time = Time()
Jack = agent.Agent(name="Jack", gender="male", kind="Seed", home=point.Point(4,4), job="Farmer", world=world)
Jill = agent.Agent(name="Jill", gender="female", kind="Seed", home=point.Point(8,8), job="Farmer", world=world)
Jordan = agent.Agent(name="Jordan", gender="male", kind="Seed", home=point.Point(2,3), job="Farmer", world=world)
print time.moment

while time.moment.day < 26:
    print "{-------It's " + str(time.moment.hour) + ":" + str(time.moment.minute) + "-------}"
    for agent in world.agents:
        print agent.name, agent.location.x, agent.location.y, agent.job.name
        priorities = agent.priorities
        doPriorities(priorities)
    time.moment = time.moment + time.increment
