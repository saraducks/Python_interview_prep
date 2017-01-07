from  exe_puzzle import Puzzle
from exe_bags_fighter import BagsFighterClown
from exe_goldzombieshooter import GoldZombieFighter


class MakeMoves(object):
    def __init__(self, scene):
        self.start = scene

    def move_blocks(self):
        self.last = ["zombie","shooter"]
        print "enter your next move"
        i = raw_input()
        if i not in self.last:
            res = self.next_scene(i)
        else:
            if i == "zombie":
                Map.temp.get("zombie")()
            else:
                Map.temp.get("shooter")()

    def next_scene(self, scene):
        val = Map.temp.get(scene)()


class Map(object):
    def __init__(self, scene):
        self.start = scene

    temp = {"fighter": BagsFighterClown().fighter,
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