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

        width_entry = tk.Entry(self, width=5)
        width_entry.insert(tk.END, '300')
        width_entry.grid(row=row, column=1)

        height_entry = tk.Entry(self, width=5)
        height_entry.insert(tk.END, '300')
        height_entry.grid(row=row, column=2)

        row += 1

        population_label = tk.Label(self, text='Scene pupulation:', font=imports.settings.text_font)
        population_label.grid(row=row, column=0)

        population_entry = tk.Entry(self, width=5)
        population_entry.insert(tk.END, 100)
        population_entry.grid(row=row, column=1)

        row += 1

        infects_label = tk.Label(self, text='Initial infects:', font=imports.settings.text_font)
        infects_label.grid(row=row, column=0)

        infects_entry = tk.Entry(self, width=5)
        infects_entry.insert(tk.END, 5)
        infects_entry.grid(row=row, column=1)

        row += 1


        self.pack()
