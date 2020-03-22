import source.imports as src

x = src.Scene(500, 500)
x.addRandomPeople(100)
x.infectRandom(5)
src.start_screen(x)
