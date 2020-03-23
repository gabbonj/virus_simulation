import source.imports as src

screen_thread = src.threading.Thread(target=src.start_screen, daemon=True)
data_thread = src.threading.Thread(target=src.start_data, daemon=True)

src.settings.main_scene = src.Scene(500, 500)
src.settings.main_scene.addRandomPeople(100)
src.settings.main_scene.infectRandom(5)
src.settings.running = True

screen_thread.start()
data_thread.start()

screen_thread.join()
data_thread.join()
print(src.settings.data)
