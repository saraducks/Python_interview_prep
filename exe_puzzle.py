import random

class Puzzle(object):                                     # class will contains simple methods and object is passed as param
    def solve_puzzle(self):
        print("what's your favorite number?")
        i = int(raw_input())
        count = 1
        if(i < 90):
            print "You are loser!!! go back!" \
                  "I wont open the door" \
                  "you have chosen unlucky number" \
                  "I can give you one more chance. try"
            while(not count > 1):
                self.solve_puzzle()
                count += 1

        else:
            print "good try! you can proceed" \
                  "you are genious than I expected"


    def win_a_mad_scientist(self):
        print "I am the genius in the world" \
              "you bet? can you beat me?" \
              "let's play if you lose you will" \
              "die with my chemicals" \
              "let's spin the wheel!"
        temp = random.randrange(1,20)
        if temp > 15:
            print "aww you won!" \
                  "get lost before I kill you"
        else:
            print "Haha I am the king, you will die now"



