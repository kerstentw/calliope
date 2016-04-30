'''
Deprecated and folded into the post_handler module.
'''

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



