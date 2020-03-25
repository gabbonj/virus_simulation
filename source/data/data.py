from .. import imports

def listen_data():
    listener = imports.Listener(imports.settings.main_scene)

    while imports.settings.running:
        listener.update()
        imports.sleep(imports.settings.sample_rate)
        imports.settings.data = listener.data
