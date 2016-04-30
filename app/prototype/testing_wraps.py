'''
This is a module that holds the wrappers
that do testing and other work for this stupid idea.

pre-import requirements:

time,
'''

import time

def time_me(func):
    def time_me(data):
        initial = time.time()
        func(data)
        end = time.time()
        diff = end - initial
        
        dic_info = {"Initial: " : initial,
        "End: " : end,
        "Total: " : diff}
        
    return time_me


#TESTING#

'''

@time_me
def adder(sync = 10):
    count = 0
    while count < sync:
        print "count It: %s \n" % count
        time.sleep(1)
        count += 1

adder(10)


'''
