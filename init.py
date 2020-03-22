import source.imports as src

x = src.Scene(500, 500)
x.addRandomPeople(100)
x.infectRandom(1)
print(x)
print(src.settings.running)
src.start_screen(x)
print(src.settings.running)
