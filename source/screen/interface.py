from .. import imports
tk = imports.tk

class Interface(tk.Frame):
    
    def __init__(self, master=None):
        row = 0
        tk.Frame.__init__(self, master)
        master.resizable(False, False)


        title = tk.Label(self, text='Virus simulation', font=imports.settings.title_font, fg='red')
        title.grid(row=row)

        row += 1

        scene_label = tk.Label(self, text='Scene settings:', font=imports.settings.section_font, fg='blue')
        scene_label.grid(row=row, column=0)

        row += 1

        dimention_label = tk.Label(self, text='Scene dimention:', font=imports.settings.text_font)
        dimention_label.grid(row=row, column=0)

        self.width_entry = tk.Entry(self, width=5)
        self.width_entry.insert(tk.END, '300')
        self.width_entry.grid(row=row, column=1)

        self.height_entry = tk.Entry(self, width=5)
        self.height_entry.insert(tk.END, '300')
        self.height_entry.grid(row=row, column=2)

        row += 1

        population_label = tk.Label(self, text='Scene pupulation:', font=imports.settings.text_font)
        population_label.grid(row=row, column=0)

        self.population_entry = tk.Entry(self, width=5)
        self.population_entry.insert(tk.END, 100)
        self.population_entry.grid(row=row, column=1)

        row += 1

        infects_label = tk.Label(self, text='Initial infects:', font=imports.settings.text_font)
        infects_label.grid(row=row, column=0)

        self.infects_entry = tk.Entry(self, width=5)
        self.infects_entry.insert(tk.END, 5)
        self.infects_entry.grid(row=row, column=1)

        row += 1

        start_button = tk.Button(self, text='Start simulation', command=self.start_simulation)
        start_button.grid(row=row, column=0)
        plot_button = tk.Button(self, text='Plot data', command=self.plot_data)
        plot_button.grid(row=row, column=1)

        row += 1

        self.pack()

    def start_simulation(self):
        screen_thread = imports.threading.Thread(target=imports.start_screen, daemon=True, name='Screen')
        imports.settings.running = True
        imports.settings.main_scene = imports.Scene(int(self.width_entry.get()), int(self.height_entry.get()))
        imports.settings.main_scene.addRandomPeople(100)
        imports.settings.main_scene.infectRandom(5)
        screen_thread.start()

    def plot_data(self):
        try:
            plotter_thread = imports.threading.Thread(target=imports.plot_data, daemon=True, name='Plotter')
            plotter_thread.start()
        except:
            print('pino')
