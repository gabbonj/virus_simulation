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

        people_label = tk.Label(self, text='People settings', font=imports.settings.section_font, fg='blue')
        people_label.grid(row=row, column=0)

        row += 1

        people_size_label = tk.Label(self, text='People size:', font=imports.settings.text_font)
        people_size_label.grid(row=row, column=0)
        
        self.people_size_entry = tk.Entry(self, width=5)
        self.people_size_entry.insert(tk.END, imports.settings.pearson_size)
        self.people_size_entry.grid(row=row, column=1)

        row += 1

        people_hitbox_radius_label = tk.Label(self, text='People hitbox radius:', font=imports.settings.text_font)
        people_hitbox_radius_label.grid(row=row, column=0)

        self.people_hitbox_radius_entry = tk.Entry(self, width=5)
        self.people_hitbox_radius_entry.insert(tk.END, imports.settings.hibox_radius)
        self.people_hitbox_radius_entry.grid(row=row, column=1)

        row += 1

        velocity_label = tk.Label(self, text='Velocity range:', font=imports.settings.text_font)
        velocity_label.grid(row=row, column=0)

        self.min_velocity_entry = tk.Entry(self, width=5)
        self.min_velocity_entry.insert(tk.END, imports.settings.min_speed)
        self.min_velocity_entry.grid(row=row, column=1)

        self.max_velocity_entry = tk.Entry(self, width=5)
        self.max_velocity_entry.insert(tk.END, imports.settings.max_speed)
        self.max_velocity_entry.grid(row=row, column=2)

        row += 1

        start_button = tk.Button(self, text='Start simulation:', command=self.start_simulation)
        start_button.grid(row=row, column=0)

        row += 1

        plot_button = tk.Button(self, text='Plot data', command=self.plot_data)
        plot_button.grid(row=row, column=0)

        row += 1

        self.pack()

    def start_simulation(self):
        screen_thread = imports.threading.Thread(target=imports.start_screen, daemon=True, name='Screen')
        imports.settings.running = True
        imports.settings.pearson_size = int(self.people_size_entry.get())
        imports.settings.hibox_radius = int(self.people_hitbox_radius_entry.get())
        imports.settings.min_speed = int(self.min_velocity_entry.get())
        imports.settings.max_speed = int(self.max_velocity_entry.get())
        imports.settings.main_scene = imports.Scene(int(self.width_entry.get()), int(self.height_entry.get()))
        imports.settings.main_scene.addRandomPeople(int(self.population_entry.get()))
        imports.settings.main_scene.infectRandom(int(self.infects_entry.get()))
        screen_thread.start()

    def plot_data(self):
        plotter_thread = imports.threading.Thread(target=imports.plot_data, daemon=True, name='Plotter')
        plotter_thread.start()
