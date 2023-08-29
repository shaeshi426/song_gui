import tkinter as tk
from tkinter import ttk
from playsound import playsound

class MP3Player:
    def __init__(self, master):
        self.master = master
        self.master.title("Play MP3 File")

        style = ttk.Style()
        style.configure("TFrame", background="#333")
        style.configure("TLabel", background="#333", foreground="#FFF", font=("Helvetica", 14))
        style.configure("TEntry", background="#FFF", foreground="#333", font=("Helvetica", 14), padding=10)
        style.configure("TButton", background="#FF3333", foreground="#333", font=("Helvetica", 14), padding=10)

        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()

        window_width = 400
        window_height = 300

        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)

        self.master.geometry('{}x{}+{}+{}'.format(window_width, window_height, x, y))

        main_frame = ttk.Frame(self.master, padding=20)
        main_frame.grid(column=0, row=0, sticky="nsew")
        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0, weight=1)

        input_label = ttk.Label(main_frame, text="name")
        input_label.grid(column=0, row=0, pady=10, sticky="w")
        self.input_field = ttk.Entry(main_frame)
        self.input_field.grid(column=0, row=1, padx=10, pady=10, sticky="we")

        play_button = ttk.Button(main_frame, text="Play MP3", command=self.play_mp3)
        play_button.grid(column=0, row=2, pady=10, padx=120, sticky="s")

    def play_mp3(self):
        name = self.input_field.get()
        print(f"Playing MP3 file for {name}")
        playsound(file)

if __name__ == "__main__":
    root = tk.Tk()
    file = ''
    MP3Player(root)
    root.mainloop()
