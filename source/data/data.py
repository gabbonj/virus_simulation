from .. import imports

def start_data():
    listener = imports.Listener(imports.settings.main_scene)

    while imports.settings.running:
        listener.update()
        imports.sleep(imports.settings.sample_rate)

    print(1)
    imports.settings.data = listener.data
    imports.plot_data()