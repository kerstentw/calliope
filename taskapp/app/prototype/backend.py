#!usr/bin/python2.7
#i
# R & D
#Contains: 
# Classes = [TimeBase, Timer, Post, FakeBase] 
#
# This is an app for writing down ideas
# After you set up a 'notebook' you have to log on and add a new idea of a minimum size
# A user must add an idea once every 24 hours
# If the user adds after some predetermined time, they are gifted bitcoin.
# If they fail to add, the timer resets and they are sent a curt message.

from time_modules import *
import os,sys
import shelve, time, threading



class TimeBase(object):

    import time

    base = time.localtime()			
	

    def __setattr__(self,*args):
        print "This object cannot be edited once created"

    def __getattr__(self,attr):
        if attr != 'base':
            print "timeBase only serves bases"


class Timer(object):

    '''
    This object will exist as a counter.  
    At instantiation it creates a base, 
    '''

    def __init__(self):
        self.creation_time = TimeBase()
        #Need a way that each time a class is un-shelved
        #it can be 

		

    def fail(self):
        '''
        Run this if user fails to do stuff.
        '''
        self.creation_time = TimeBase()



class UserPost(object):

    def __init__(self):
        self.creationTime = Timer()
        self.MAX_LEN = 300
        self.MIN_LEN = 250
        self.post_log = {} 


    def __verifyPost(self,post):
        
            '''
        can't verify data...
        returns a tuple: (bool, verification message)
            '''

        #try:
            test_len = len(str(post))

            if test_len < self.MIN_LEN or test_len > self.MAX_LEN:
                return (False, "Post must be between 250 and 300 characters.")

    
            else:
                return (True,"Verified")

        #except:
            return (False, "Problem with dataflow. SiteError 5")
        
       

    def __writeToDatabase(self,data):
        pass     

    def logReport(self):
        if self.post_log:
            print "Time Created : {}".format(self.post_log["TimeCreated"])
            print "Post Info : {}".format(self.post_log["PostInfo"])

        else:
            return

    def createPost(self,post_text = None):
        
        verification = self.__verifyPost(post_text)

        if not verification[0]:
            return "Char, Error: {error_msg}\nPost not created.".format(
                                            error_msg = verification[1])
        
        self.post_log["TimeCreated"] =  Timer().creation_time.base
        self.post_log["PostInfo"] = post_text
        

                        
        
    


###TEST####

class FakeRequest(object):
    def __init__(self):
        pass

