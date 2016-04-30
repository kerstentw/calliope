#customUserDict

from UserDict import UserDict

class ControllerDict(UserDict):
    def __init__(self):
        UserDict.__init__(self)

    def __setitem__(self,key,value):
        try: 
            self.data[key] = value

        except KeyError:
            raise KeyError,"Key does not exist in ControllerDict obj."


    def __getitem__(self,key):
        try:
            return self.data[key]

        except KeyError:
            raise KeyError
            return

        except ValueError:
            raise ValueError


def postdict():
    postdict = ControllerDict()
    return postdict

