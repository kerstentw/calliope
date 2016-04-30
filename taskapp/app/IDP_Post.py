#!usr/bin/python2.7

import hashlib
#import db_helper #Has functions for interacting with test database
import os
import sys
import PostDict
import time, datetime
from constants import *



class IdeaCollection(object):
    
    '''
    This class creates an ovject that keeps track of the posting
    dates and times.  It is what is read off of to insure that a 
    user gets paid, posts regularly, and keeps a running record
    of a user's stuff.

    '''

    def __init__(self, password = "Test"):
        
        '''
        This constructor will create a password hash that can be
        used to verify user.
        '''

        if password: 
            passhash = hashlib.sha256(str(password)).hexdigest()

        else:
            passhash = hashlib.sha256("key").hexdigest()        

        self.passhash = passhash

        datetime.MINYEAR = 2016
        build_time = tuple(x for x in time.localtime()[0:5])
        
        self.creationtime = build_time
        self.last_post = build_time
        self.current_time = build_time

        #Eventually use self.hashlist as a way to merge IdeaPads.
        self.hashlist = ['END'] # Treat as a reverse queue: front is oldest.  Tail is youngest
        self.payMe = True
        self.name = str(passhash)
    
        self.post_texts = PostDict.postdict()  

   
    def __convertToDateTime(self,time_tuple):
        '''
        convert a time tuple into a datetime structure
        '''

        time_str = "datetime.datetime{}".format(time_tuple)
        datetime_obj = eval(time_str)
        print datetime_obj
        return datetime_obj


    def coerceCurrentAnchorChange(self,(yyyy,mm,dd,hh,ss),just_current = 1):
        
        '''
        FOR DEVELOPMENT/DEPLOYMENT TESTING ONLY!!!!!!!!!!!!!!!!!!!

        coerceCurrentAnchorChange((yyyy,mm,dd,hh,ss)[,just_current = 1])        

        for testing, allows an anchor to be changed from the shell
        takes a tuple of (yyyy,mm,dd,hh,ss) and if just current is
        set to 0, will rebuild the anchor (the last date of successful post.
        
        need to comment out self.updatePost in checkElapsedTime 

        '''
        
        self.current_time = (yyyy,mm,dd,hh,ss)

        if just_current == 0:
            self.last_post = self.current_time
        else:
            pass


    def updatePost(self):
        self.current_time = tuple(x for x in time.localtime()[0:5])


    def checkElapsedTime(self):
        self.updatePost()
        dt_last_post = self.__convertToDateTime(self.last_post)        
        dt_current = self.__convertToDateTime(self.current_time)
        elapsed = dt_current - dt_last_post        

        return elapsed.days       


    def postSuccessfullyMade(self):
        self.last_post = tuple(x for x in time.localtime()[0:5])


    def checkForPayment(self):
        elapse_check = self.checkElapsedTime()
        if elapse_check  == 0:
            self.payMe = True
            return self.payMe       
 
        elif elapse_check > 0:
            self.payMe = False
            return self.payMe

        else: # Implies error.  Assume status does not change.
            return self.payMe


    def reHash(self,new_pass):
        self.hashdict.append(self.passhash)
        self.passhash = hashlib.sha256(new_pass)


    def stat(self):
        self.updatePost()
        my_stats = { 'name'          : self.name,
                     'password_hash' : self.passhash,
                     'creation_date' : self.creationtime,
                     'last_post'     : self.last_post,
                     'last_checked'  : self.current_time,
                     'payable?'      : self.payMe
                   }

        return my_stats


    def delete(self,master = PICKLE_MASTER): #from constants library
        os.remove(os.path.join(PICKLE_MASTER,self.name))
        return self.name," Removed"
 
 
    def addPost(self,post_name = "Default", post_info = "D" * 250):

        '''
		Adds idea_post_string into the Post
        '''

        try:
            if len(post_info) > 300:
                return "Submission failed, Too many characters, must be less than 300 characters."


            elif len(post_info) < 200:
                return "Submission failed: Too few characters, must be greater than 200 characters."            
            else:

                self.post_texts[post_name + "::"+ str(self.current_time)] = post_info
                return "Post successfully made"
        
        except:
	    return "Unknown error while posting"  

          
    def fetchAllPosts(self):
        """
		Returns a tuple of posts that can be paginated by the front end
		to show the user.
        """
		
        return tuple((post,self.post_texts[post]) for post in 
                                                   self.post_texts.data)
		
		
		
