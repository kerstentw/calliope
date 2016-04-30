#customUserDict

from UserDict import UserDict

class ControllerDict(UserDict):
    def __init__(self):
        UserDict.__init__(self)

    def __setitem__(self,key,value):
        value = str(value)
        if len(value) > 300:
            print "Too many characters. CharCount needs to be  between 200 and 300"
            return
        elif len(value) < 200:
            print "Too few characters.  CharCount needs to be between 200 and 300"


        self.data[key] = value

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

