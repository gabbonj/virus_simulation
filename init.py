import source.imports as src


src.settings.main_scene = src.Scene(500, 500)
src.settings.main_scene.addRandomPeople(100)
src.settings.main_scene.infectRandom(5)
src.settings.running = True

app = src.App()
app.run()


print(src.settings.data)
