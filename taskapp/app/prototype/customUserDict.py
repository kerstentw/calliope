#customUserDict

from UserDict import UserDict

class ControllerDict(UserDict):
    def __init__(self):
        UserDict.__init__(self)

    def __setitem__(self,key,value):
        value = str(value)
        if len(value) > 300 or len(value) < 250:
            print "value needs to be between 250 and 300"
            return

        self.data[key] = value

    def __getitem__(self,key):
        return self.data[key]



def postdict():
    postdict = ControllerDict()
    return postdict

