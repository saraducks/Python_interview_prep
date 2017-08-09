from  exe_puzzle import Puzzle
from exe_bags_fighter import BagsFighterClown                  # import the .py files
from exe_goldzombieshooter import GoldZombieFighter

temp_move_record = []                                          # empty list

class MakeMoves:

    def __init__(self, scene):                                 # initialize with the start move
        self.start = scene
        temp_move_record.append(scene)
        self.next_scene(scene)

    def move_blocks(self):                                    # this will itertate till 8 moves, user can't repeat the
        count = 8                                             # moves. The empty list will get accumulate with moves.
        while(count > 0):
            self.last = ["zombie","shooter"]
            print "enter your next move"
            i = str(raw_input())

            if i not in (self.last):                           # if condition checks if it is last move or the move made already
                if i in temp_move_record:
                    print "you cannot make the same move again!" \
                          "Try another move"
                else:
                    res = self.next_scene(i)

            else:
                if i == "zombie":
                    Map.temp.get("zombie")()
                else:
                    Map.temp.get("shooter")()
            count = count - 1
            temp_move_record.append(i) if i not in temp_move_record else "do nothing"
        del temp_move_record[:]

    def next_scene(self, scene):                              # this will invoke the dictionary stored into the MAP class
        val = Map.temp.get(scene)()


class Map(object):
    def __init__(self, scene):
        self.start = scene

    temp = {"fighter": BagsFighterClown().fighter,           # dictionary of key and functions as values
            "puzzle": Puzzle().solve_puzzle,
            "madman": Puzzle().win_a_mad_scientist,
            "clown": BagsFighterClown().clown,
            "bags": BagsFighterClown().bags,
            "gold": GoldZombieFighter().gold_room,
            "zombie": GoldZombieFighter().zombie_room,
            "shooter": GoldZombieFighter().shooter_room,
            }


t = Map("fighter")
m = MakeMoves("fighter")
m.move_blocks()