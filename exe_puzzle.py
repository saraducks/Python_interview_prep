import random

class Puzzle(object):
    def solve_puzzle(self):
        print("what's your favorite number?")
        i = raw_input()
        if(i > 90):
            print "good try! you can proceed"

        else:
            print "You are loser!!! go back!"

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



