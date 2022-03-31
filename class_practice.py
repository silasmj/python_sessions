from ast import arg


class Person:
    #class variables
    type = 'Mammel'


    def __init__(self, *args, **kwargs):
        self.name = args[0] # instance variable
        print(args)
        print(kwargs)
    
    def msg(self):
        return 'Hello'

