from art import text2art
from random import randint


class Banner:
    def __init__(self, text, font="georgia11"):
        self.text = text
        self.font = font

    def random_banner(self):
        fonts = ["1943", "3-d", "3d_diagonal", "4max", "5lineoblique", "6x10", "a_zooloo", "alligator2", "alligator3",
                 "amcaaa01", "amcneko", "amcslash", "arrows", "ascii_new_roman", "avatar", "basic", "bell", "big",
                 "bigfig", "bolger", "braced", "bulbhead", "calgphy2", "chiseled", "chunky", "crawford", "cricket",
                 "cyberlarge", "cybermedium", "defleppard", "doom", "double", "epic", "filter", "fire_font-s",
                 "fraktur", "georgia11", "ghost", "ghoulish", "graffiti", "isometric1", "isometric4", "jacky",
                 "larry3d", "lean", "lineblocks", "merlin1", "modular", "rammstein", "red_phoenix", "rounded", "slant",
                 "speed", "starwars", "stop", "sub-zero", "swampland", "twisted"]
        return text2art(self.text, font=fonts[randint(0, len(fonts) - 1)])

    def __str__(self):
        return text2art(self.text, font=self.font)
