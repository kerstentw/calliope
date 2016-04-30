#!/usr/bin/Python2.7

#PostManager is a module for handling Posts.  It directly interfaces
# with the Post module and instances Posts
# It does:
#    -instantiate posts
#    -Pickle Posts
#    -Place pk files in db
#    -Manage Posts

# use post_instance.stat() to get a dump of a posts's 
#contents for db write.
# Purposely made the stat method a Python DataStruc in order to make it
# compatible with any db.

# Author: Tai Kersten
# Email: kerstentw@gmail.com
import console
import os, sys
import hashlib
import cPickle
from .IDP_Post import *
    # instantiates the term 'Post' with all its methods.


#If a new instance, will create the home dir 
#necessary for the functioning of the manager

PICKLE_MASTER = "pk_jar"

if PICKLE_MASTER not in os.listdir('.'):
    os.mkdir(PICKLE_MASTER)

else:
    pass


class PickleManager(object):

    '''
            Pickles will be stored locally at first then in the database
after the site has been migrated to a proper storage facility.
Use Django's modeling system to build out these databases adn their 
entry points.  Use the db_helper to set up modeling for data that is 
going to get pushed.  See if a PSQL offsite is possible.  
  
    '''
	
        
    def __init__(self, master = PICKLE_MASTER):
        from .IDP_Post import *
        self.master = PICKLE_MASTER

    def picklePosts(self,post_instance):
        
        '''
        This function pickles an instance of a post and writes it to the master
        folder defined above.
        

        '''
        
 
        temp_file = open(os.path.join(
                              self.master,
                              "{post_name}.pk".format(
                              post_name = post_instance.name)),"wb")
                              
        unpickled_post = cPickle.dump(post_instance,temp_file)
        temp_file.close()

        return "post saved"


    def viewPicklesInJar(self):
        return os.listdir("pk_jar")    
        
    def dePickle(self, pickle_human_name):
        
        '''
        this will pull out a pickled Post object.
        Returns entire object so methods need to be referenced directly
        from the variable that it has been placed inside.        
        '''
        #When calling this, use a try-except loop
        
        pickle_human_name = str(pickle_human_name)
        pickle_name = hashlib.sha256(pickle_human_name).hexdigest() + ".pk"
        full = os.path.join(PICKLE_MASTER,pickle_name)
        full = os.path.join(os.curdir,full)

        my_pickle = open(full,"rb")
        
        post_instance = cPickle.load(my_pickle) 
        
        return post_instance


    def pushPK(self): #To Database
        pass


    def deletePickle(self,human_readable_name):
        #Need superUser permissions...
        
        pickle_name = hashlib.sha256(str(human_readable_name))
        picks = os.listdir(os.path.join(os.curdir,PICKLE_MASTER))
        
        if pickle_name in picks:
			os.remove(os.path.join(picks,pickle_name))

        return human_readable_name, " deleted"









#####
##### FIGURE OUR DATAFLOW FOR THIS MOTHERFUCKER
#####



class PostManager(object):

    '''
    This handles retrieving info from the Post objects.  It has no 
methods for database or pickle management directly.  It is primarily 
handled by two things:

		- The front end (HTML, GUI app)
		- The Pickle Manager.
		
	Keep in mind that the PostManager does not hold any state and has
no built in methods for retrieving any saved state whether from a 
session or a pickle.
    
    Each new reference or change must accompany a depickling of the 
post instance.  This is to prevent 
    '''

    def __init__(self,post_instance = None):
        self.spm = PickleManager() #spm is Session Pickle Manager


    def create_post(self,username):
        '''
		This function relies on the frontend's ability to ensure that 
all usernames being stored in the user_database are unique.  Any repeats
will cause problems.
        '''
		
        new_post = IdeaCollection(username)
        self.spm.picklePosts(new_post)
        return "Post Created."


    def fetchPost(self,username):
        '''
        Wrap in a try/except IOError
        '''
        post_instance = self.spm.dePickle(username)
        return post_instance
    
    def makeSubmission(self,post_instance,name,data):
        try:
            status = post_instance.addPost(name,data)
            self.spm.picklePosts(post_instance)
            return status
        except:
            return "Error Submitting"

    def checkForPayment(self,post_instance):
        if post_instance:
            return post_instance.checkForPayment()

    def stat_post(self,post_instance):
        return  post_instance.stat()
    
    def displayPosts(self,post_instance):
		
        post_list = post_instance.fetchAllPosts()
        return post_list
        
