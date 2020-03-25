from . import imports

class App():

    def __init__(self):

        self.interface_thread = imports.threading.Thread(target=self.runInterface, daemon=True, name='Iterface')
        self.listener_thread = imports.threading.Thread(target=self.runListener, daemon=True, name='Listener')
        self.plotter_thread = imports.threading.Thread(target=self.runPlotter, daemon=True, name='Plotter')
        self.screen_thread = imports.threading.Thread(target=self.runScreen, daemon=True, name='Screen')

    def runInterface(self):
        root = imports.tk.Tk()
        self.interface = imports.Interface(master=root)
        self.interface.mainloop()

    def runScreen(self):
        imports.start_screen()

    def runListener(self):
        imports.listen_data()

    def runPlotter(self):
        imports.plot_data()

    def run(self):
        self.screen_thread.start()
        self.interface_thread.start()
        self.listener_thread.start()

        self.interface_thread.join()
        imports.settings.running = False
        self.plotter_thread.start()
        self.plotter_thread.join()
