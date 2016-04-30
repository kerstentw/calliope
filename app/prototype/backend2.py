#!usr/bin/python2.7

import hashlib
import os
import sys
import time, datetime


class Post(object):
    
    '''
    This class creates an ovject that keeps track of the posting
    dates and times.  It is what is read off of to insure that a 
    user gets paid, posts regularly, and keeps a running record
    of a user's stuff.
    '''

    def __init__(self, password = None):
        if password: self.passhash = hashlib.sha256(password)

        datetime.MINYEAR = 2016
        self.creation_time = tuple(x for x in time.localtime()[0:5])
        
        self.last_post = self.creation_time
        self.current_time = self.creation_time
        self.payMe = True


    def __convertToDateTime(self,time_tuple):
        time_str = "datetime.datetime{}".format(time_tuple)
        datetime_obj = eval(time_str)
        print datetime_obj
        return datetime_obj

    def coerceCurrentAnchorChange(self,(yyyy,mm,dd,hh,ss),just_current = 1):
        
        self.current_time = (yyyy,mm,dd,hh,ss)

        if just_current == 0:
            self.last_post = self.current_time
        else:
            pass

    def updatePost(self):
        self.current_time = tuple(x for x in time.localtime()[0:5])


    def checkElapsedTime(self):
        self.updatePost()
        dt_last_post = self.__convertToDateTime(self.post_anchor)        
        dt_current = self.__convertToDateTime(self.current_time)
        elapsed = dt_current - dt_last_post        

        return elapsed.days       

    def postSuccessfullyMade(self):
        self.last_post = tuple(x for x in time.localtime()[0:5])

    def checkForPayment(self):
        if self.checkElapsedTime() == 0:
            self.payMe = True
            return self.payMe       
 
        elif self.checkElapsedTime() > 0:
            self.payMe = False
            return self.payMe
