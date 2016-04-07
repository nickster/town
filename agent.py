#!/usr/bin/python

import random
import point
import occupations

class Agent(object):
    'Base class for all agents. Creates an agent including where they start and gives them a set of priorities, with their job at the top of the list.'
    
    def __init__(self, name, gender, kind, home, job, world):
        self.name = name
        self.unique = name + str(random.choice(range(0,1000)))
        self.gender = gender
        self.kind = kind
        self.location = point.Point(home.x,home.y)
        self.home = point.Point(home.x,home.y)
        if job == "Farmer":
            self.job = occupations.Farmer(self)
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