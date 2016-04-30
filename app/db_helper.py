#!/usr/bin/python2.7
'''
    Holds the database modeling information for the app.  Eventually,
this will be deprecated in favor of using Django's modeling system.

'''

try:
    import psycopg2
    import pickle
    import sqlite3

except:
    pass

def pickle_it(to_pickle, mode = "w"):

    '''
    mode types : 'w'
    '''
    
    if mode == "w":
        file_to_pickle = open("{}.pk".format(to_pickle.name),mode)
        pickle.dump(to_pickle,file_to_pickle)
        file_to_pickle.close()
        print "File {filename} state preserved to: {filename}.pk".format(filename = to_pickle.name)

    if mode == "r":
        file_to_pickle = open("{}.pk".format(to_pickle.name),mode)
        dumped = pickle.load(file_to_pickle)
        print "{} loaded into memory.".format(to_pickle.name) 
        return dumped 
