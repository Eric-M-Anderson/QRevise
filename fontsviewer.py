from banner import Banner

fonts = ["1943", "3-d", "3d_diagonal", "4max", "5lineoblique", "6x10", "a_zooloo", "alligator2", "alligator3", "amcaaa01", "amcneko", "amcslash", "arrows",
         "ascii_new_roman", "avatar", "basic", "bell", "big", "bigfig", "bolger", "braced", "bulbhead", "calgphy2", "chiseled", "chunky", "crawford", "cricket",
         "cyberlarge", "cybermedium", "defleppard", "doom", "double", "epic", "filter", "fire_font-s", "fraktur", "georgia11", "ghost", "ghoulish", "graffiti",
         "isometric1", "isometric4", "jacky", "larry3d", "lean", "lineblocks", "merlin1", "modular", "rammstein", "red_phoenix", "rounded", "slant", "speed",
         "starwars", "stop", "sub-zero", "swampland", "twisted"]

for i in fonts:
    open(r'D:\Data\4. Leisure\1. Programming\Python Programs\Text Editor\QRevise\Fonts.txt', "a").write('{0}\n\n{1}\n\n\n'.format(i, Banner('QRevise', i)))

# big
# doom
# epic
# georgia11
# jacky
# slant
