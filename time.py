#!/usr/bin/python

import datetime

class Time(object):
    #The hand of everything
    def __init__(self):
        self.moment = datetime.datetime(year=2015,month=5,day=25,hour=0)
        self.increment = datetime.timedelta(minutes=60)