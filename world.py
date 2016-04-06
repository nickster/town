#!/usr/bin/python

import pdb
import datetime
import random
        
"""

WHERE IS THIS GOING???

"Every day the things we do change us. Some subtle, some profound, until we are no longer ourselves."

An agent-based model that demonstrates how events in a village can dramatically shape people's lives over weeks, months, and years. Observable by a top-down map, with agents color-coded by emotional state, noted by age + gender, with icon for current priority. Plus a log of notable events.

Eventually, two AI engines power the agents:

Learning-based: Agents access their memories to borrow strategies to accomplish goals
Planning-based: If no known path to a goal exists, agents use a version of the world and iterate on it to discover a path to their strategy

Guiding principles:
    When adding a new dimension to the simulation, don't add more than two properties to it at first. For example, no more than two jobs, no more than two personality traits, etc. Get the engine working well before adding more complexity.
    Resist the urge to mirror our real-world. Create new behaviors, concepts, and simplify. Minecraft is fun because it has it's own rules, own language.
    The world is subjective.

***

PROJECTS

Short-term & interesting
    shared space is creating the same dictionary for different agents. it also doesn't get called from the activity_update because being at home doesn't have an activity. Need some lazy-state activity that comes in so that it is triggered while at home.
    Positive and negative bonds form slowly by doing activities in the same space
        Probability of a positive or negative micro-interaction is directly related to your current relationship
    Clear out activities when completed
    Social activities are based on feelings
    dinner time needs to adjust to when people get home
    Create more independent priorities
        Plug in
    Social priorities
        Make love
        Play with kids
        Play with friends
    Days of the week
    Print logs in sensible, tabular format
        Agent - role - going to do - location

Programming quality
    Priorities inherit a parent which includes activity_update
    Make jobs less hacky when the agent is called. Find a way to use an argument to class conversion
    Append simplicity
    wtf are private vs. public functions? refresh on advanced programming. this will make a big difference. including style guides.
    self isn't used in the commute logic
    How do you create two separate instances of one variable gracefully (not a pointer)

Long-term
    Negative relationships form
    Witnesses tell friends who tell other friends... information passes on
    Different occupations
    Visual representation
    spacial awareness & basic social interaction
    Randomness
    Hierarchy of needs. Defined by priority levels? General template, but personalized.
    Create a larger world map of 3 houses, school, office, farm, restaurant/bar, park, gym
    Planning behavior vs. habit. If no behavior exists, flip a coin? Could also be based on traits.
    The impact that a behavior has on a witness' mood is tied to the intent, strength of the relationship, empathy with those in the situation, and level of independence of the witness. Associations change over time. Mood impacts underlying characteristics.
    Data repeatedly observed becomes a belief
    Lies
    Create traits & moods that will influence behaviors
    Traits change slowly over time, mood vary more widely
    Meyers Brigg?
        Extrovert vs. Introvert - Impact social routine, family routine, encounters, and work style
        Judging vs. Perceiving - Structured vs. spontaneous
    Moods
        Positive vs. negative - Happy increases quality/ speed of behavior, sad decreases it. Both can create new behaviors/ cancel behaviors.
        Energetic vs. relaxed
    Economics
    Triggers - Seeing something good or bad happen in your space impacts mood
    Darkness: Sickness and death, depression, alcoholism, drugs, violence, crime
    World is randomly generated
    Model goes beyond a day
    One-second increments
    Agents have memory. Used for AI. Memory is not just what they experience personally but what they observe, including on TV.


"""

class Agent(object):
    'Base class for all agents. Creates an agent including where they start and gives them a set of priorities, with their job at the top of the list.'
    
    def __init__(self, name, gender, kind, home, job, world):
        self.name = name
        self.unique = name + str(random.choice(range(0,1000)))
        self.gender = gender
        self.kind = kind
        self.location = Point(home.x,home.y)
        self.home = Point(home.x,home.y)
        if job == "Farmer":
            self.job = Farmer(self)
        else:
            self.job = Student(self)
        self.family = Family(self)
        self.social_graph = {}
        self.priorities = []
        self.priorities.append(self.job)
        self.priorities.append(self.family)
        self.priorities.append(Eat(self))
        self.activity = {"primary":"None","secondary":"None"}
        self.values = ["eating", "sleeping","working","studying","playing"]
        world.agents.append(self)
        
    def activity_update(self, activity_to_check):
        near = agents_at_point(world.x[self.location.x], world.y[self.location.y])
        for agent in near:
            if self.social_graph.__contains__(agent.unique) == False:
                self.social_graph[agent.unique] = [0,agent]
        activity = activity_to_check
        if self.values.index(activity) < self.activity["primary"]:
            self.activity["primary"] = activity
            print agent.name + " is " + activity
                
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

class Farmer(object):
    'Creates a farmer occupation tailored to an agent.'
    
    def __init__(self, agent):
        self.name = "Farmer"
        self.activity = "working"
        self.agent = agent
        self.location = Point(5,5)
        self.starttime = 7 #In hour of the day
        self.endtime = 16 #In hour of the day
        self.priorities = []
        self.priorities.append(Commute(self.agent, self.starttime, self.endtime, self.location))
        
    def do(self):
        if self.endtime > int(time.moment.hour)  > self.starttime:
            self.agent.activity_update(self.activity)
        pass
    
class Student(object):
    'Creates a student occupation tailored to an agent.'
    
    def __init__(self, agent):
        self.name = "Student"
        self.activity = "studying"
        self.agent = agent
        self.location = Point(6,6)
        self.starttime = 9 #In hour of the day
        self.endtime = 15 #In hour of the day
        self.priorities = []
        self.priorities.append(Commute(self.agent, self.starttime, self.endtime, self.location))
        
    def do(self):
        if self.endtime > int(time.moment.hour)  > self.starttime:
            self.agent.activity_update(self.activity)
        pass

class Eat(object):
    'Defines meal-seeking behavior'
    
    def __init__(self, agent):
        self.agent = agent
        self.activity = "eating"
        self.breakfast_time = 7
        self.lunch_time = 13
        self.dinner_time = 20
        
    def do(self):
        if ((int(time.moment.hour) == self.breakfast_time) or (int(time.moment.hour) == self.lunch_time) or (int(time.moment.hour) == self.dinner_time)):
            self.agent.activity_update(self.activity)

class Commute(object):
    'Being assigned a job instantiates a Commute object within the job priority list. This containts the commute.do'

    def __init__(self, agent, starttime, endtime, location):
        self.agent = agent
        self.starttime = starttime
        self.endtime = endtime
        self.location = location
        self.morningcommutetime = self.set_morning_commute_time(self.starttime)
        self.nightcommutetime = datetime.timedelta(hours=self.endtime)
    
    def set_morning_commute_time(self, starttime):
        starttime = datetime.timedelta(hours=starttime)
        moves = abs(self.agent.home.x - self.location.x) + abs(self.agent.home.y - self.location.y)
        totalcommutetime = moves * time.increment
        return (starttime - totalcommutetime)
        
    def do(self):
        if (self.agent.location.x - self.location.x != 0 or self.agent.location.y - self.location.y !=0)  and (int(time.moment.hour) >= int(self.morningcommutetime.seconds) // 3600) and (int(time.moment.hour) < self.starttime):
            print self.agent.name + " is commuting to " + str(self.location)
            Move(self.agent).move_toward(self.location)
        'If its time to go home...'
        if  (int(time.moment.hour) >= self.endtime) and (self.agent.location.x - self.agent.home.x != 0 or self.agent.location.y - self.agent.home.y !=0):
            print self.agent.name + " is going home towards " + str(self.agent.home)
            Move(self.agent).move_toward(self.agent.home)

class Play(object):
    
    def __init__(self):
        self.agent = agent
        self.activity = "playing"
        

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
            home = Point(self.agent.home.x, self.agent.home.y)
            new_child = Agent(random.choice(name_set), gender, "Sprout", home, "Student", world)
            self.children.append(new_child)
            self.spouse.family.children.append(new_child)
            new_sibling_index = len(self.children) - 1 
            new_child.family.parents.append(self.agent)
            new_child.family.parents.append(self.spouse)
            for child in self.children:
                child.family.siblings.append(new_child)
            total = total - 1
            
    def create_spouse(self):
        home = Point(self.agent.home.x, self.agent.home.y)
        if self.agent.gender == "male":
            gender = "female"
            name_set = girls_names
        else:
            gender = "male"
            name_set = boys_names
        self.spouse = Agent(random.choice(name_set), gender, "Sprout", home, "Farmer", world)
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

class Time(object):
    #The hand of everything
    def __init__(self):
        self.moment = datetime.datetime(year=2015,month=5,day=25,hour=0)
        self.increment = datetime.timedelta(minutes=60)
        
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
boys_names = ["Crane","Hicks","Gordon","Allum","Chais","Bamtug","Reed-meed","Hillbilly","Simon Says","A.B.S","Chicago"]
girls_names = ["Mara","Kyra","Kristee", "Noor","Gia","Gwen","Bertha", "Charlene","Quizza","Maya-Angelou","Emily Dickinson"]
time = Time()
Jack = Agent(name="Jack", gender="male", kind="Seed", home=Point(4,4), job="Farmer", world=world)
Jill = Agent(name="Jill", gender="female", kind="Seed", home=Point(8,8), job="Farmer", world=world)
Jordan = Agent(name="Jordan", gender="male", kind="Seed", home=Point(2,3), job="Farmer", world=world)
print time.moment

while time.moment.day < 26:
    print "{-------It's " + str(time.moment.hour) + ":" + str(time.moment.minute) + "-------}"
    for agent in world.agents:
        print agent.name, agent.location.x, agent.location.y, agent.job.name
        priorities = agent.priorities
        doPriorities(priorities)
    time.moment = time.moment + time.increment
