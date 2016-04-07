#!/usr/bin/python

import point
import priorities

class Farmer(object):
    'Creates a farmer occupation tailored to an agent.'
    
    def __init__(self, agent):
        self.name = "Farmer"
        self.activity = "working"
        self.agent = agent
        self.location = point.Point(5,5)
        self.starttime = 7 #In hour of the day
        self.endtime = 16 #In hour of the day
        self.priorities = []
        self.priorities.append(priorities.Commute(self.agent, self.starttime, self.endtime, self.location))
        
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
        self.location = point.Point(6,6)
        self.starttime = 9 #In hour of the day
        self.endtime = 15 #In hour of the day
        self.priorities = []
        self.priorities.append(priorities.Commute(self.agent, self.starttime, self.endtime, self.location))
        
    def do(self):
        if self.endtime > int(time.moment.hour)  > self.starttime:
            self.agent.activity_update(self.activity)
        pass