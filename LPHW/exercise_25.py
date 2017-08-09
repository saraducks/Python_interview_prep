'''
This class shows how __init__ works upon instantiation
'''
class demo:
    def __init__(self):
        self.guess = "I am wondering what this init does.Let's see!"

    def hello(self,user_inpput):                # This will print user input as list
        print self.guess
        temp = str.split(user_inpput,' ')
        print temp


d = demo()                                      # This line will instantiate the class
d.hello("This is my test class")                # calls the class method.
                                                # The __init__ method gets initialized during the instantiation and
                                                # It doesn't take any user input