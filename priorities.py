#!/usr/bin/python

#Need to create a parent class that takes the world and an agent. All occupations are children of this class. The time.increment is then fed to an attribute of all child classes. Need to create a separate time module.

#Move move here.

import datetime

class Priority(object):
    'Every priority is instantiated with the below parameters'

    def __init__(self, agent, time):
        self.agent = agent
        self.time = time


class Eat(Priority):
    'Defines meal-seeking behavior'
    
    def __init__(self, agent):
        self.activity = "eating"
        self.breakfast_time = 7
        self.lunch_time = 13
        self.dinner_time = 20
        
    def do(self):
        if ((int(self.time.moment.hour) == self.breakfast_time) or (int(self.time.moment.hour) == self.lunch_time) or (int(self.time.moment.hour) == self.dinner_time)):
            self.agent.activity_update(self.activity)

class Commute(Priority):
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
        totalcommutetime = moves * self.time.increment
        return (starttime - totalcommutetime)
        
    def do(self):
        if (self.agent.location.x - self.location.x != 0 or self.agent.location.y - self.location.y !=0)  and (int(self.time.moment.hour) >= int(self.morningcommutetime.seconds) // 3600) and (int(self.time.moment.hour) < self.starttime):
            print self.agent.name + " is commuting to " + str(self.location)
            Move(self.agent).move_toward(self.location)
        'If its time to go home...'
        if  (int(self.time.moment.hour) >= self.endtime) and (self.agent.location.x - self.agent.home.x != 0 or self.agent.location.y - self.agent.home.y !=0):
            print self.agent.name + " is going home towards " + str(self.agent.home)
            Move(self.agent).move_toward(self.agent.home)

class Play(Priority):
    
    def __init__(self):
        self.activity = "playing"