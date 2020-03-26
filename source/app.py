from . import imports

class App():

    def __init__(self):

        self.interface_thread = imports.threading.Thread(target=self.runInterface, daemon=True, name='Iterface')
        

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
        self.interface_thread.start()
        self.interface_thread.join()

