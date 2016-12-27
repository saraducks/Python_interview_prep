'''
class inheritance, composition
'''
class Fish(object):
    def __init__(self):
        self.fish = "I am fish"
        print self.fish
    def myguess(self):
        print "This is inside demo.myguess method"

    def basicfeatures(self):
        print "This is inside demo.basicfeatures method"
        print "Lives in water"

class salmon(object):
    def __init__(self):
        print "this is inside salmon.__init__"
        self.temp = Fish()
    def salmonfeatures(self):
        print "Looks red, long nose"
        self.temp.basicfeatures()

class tuna(Fish):
    def __init__(self):
        self.fish =  "I am tuna, a kind of fish"
        print  self.fish

    def  demo(self):
        print "I am inside tuna.demo method"
        super(tuna, self).myguess()

foo = Fish()
foo.myguess()
foo1 = salmon()
foo1.salmonfeatures()
foo2 = tuna()
foo2.demo()

