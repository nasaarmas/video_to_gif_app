import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import os
from model import FileHandler


class UIController:
    def __init__(self, controller_constructor):
        """Creating and specifying tkinter window"""
        self.controller = controller_constructor
        self.root = tk.Tk()
        self.root.title('Converting vid to gif app')
        self.wind_width = 600
        self.wind_height = 300
        self.root.geometry(self.wind_geometry())
        self.video_path = tk.StringVar()
        self.save_filepath = tk.StringVar()

        select_file_button = tk.Button(self.root, text="Select File", command=self.open_file_dialog)
        select_file_button.place(x=(self.wind_width - select_file_button.winfo_reqwidth()) / 2, y=15)

        self.text_label = tk.Label(self.root, text="")

        output_file_button = tk.Button(self.root, text="Save as", command=self.save_as_file_dialog)
        output_file_button.place(x=(self.wind_width - output_file_button.winfo_reqwidth()) / 2, y=90)

        self.text2_label = tk.Label(self.root, text="")

        to_gif_button = tk.Button(self.root, text="Convert to gif", command=self.controller.create_gif, width=20)
        to_gif_button.place(x=(self.wind_width - to_gif_button.winfo_reqwidth()) / 2, y=165)

        self.progress = ttk.Progressbar(self.root, length=200, mode='determinate')
        self.progress.place(x=(self.wind_width - self.progress.winfo_reqwidth()) / 2, y=205)

        exit_button = tk.Button(self.root, text="Exit", command=self.root.destroy)
        exit_button.place(x=(self.wind_width - exit_button.winfo_reqwidth()) / 2, y=240)

    def wind_geometry(self):
        """Defining tkinter window size and its place of opening"""
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        position_top = int((screen_height - self.wind_height) / 2)
        position_left = int((screen_width - self.wind_width) / 2)
        return f"{self.wind_width}x{self.wind_height}+{position_left}+{position_top}"

    def open_file_dialog(self):
        """Opening file explorer to choose file that will be converted"""
        self.progress['value'] = 0  # Update the progress bar
        self.root.update()  # Force tkinter to update the GUI
        current_dir = os.getcwd()  # Get the current working directory
        filepath = filedialog.askopenfilename(initialdir=current_dir)
        if filepath:
            # Pass the filepath to another function
            self.text_label.config(text=f"Path To File: {filepath}")
            self.text_label.place(x=(self.wind_width - self.text_label.winfo_reqwidth()) / 2, y=52)
            FileHandler.video_path = filepath

    def save_as_file_dialog(self):
        """Opening file explorer to choose name of converted, output file"""
        self.progress['value'] = 0  # Update the progress bar
        self.root.update()  # Force tkinter to update the GUI
        current_dir = os.getcwd()  # Get the current working directory
        filepath = filedialog.asksaveasfilename(defaultextension=".gif", initialdir=current_dir)
        if filepath:
            # Pass the filepath to another function
            self.text2_label.config(text=f"Save as: {filepath}")
            self.text2_label.place(x=(self.wind_width - self.text2_label.winfo_reqwidth()) / 2, y=132)
            FileHandler.save_filepath = filepath

    def update_progress(self, value):
        """as name suggests it is function to update progress bar"""
        self.progress['value'] += value
        self.root.update()

    def show_error(self, message, exception_placement=1):
        """function to print errors in case of exception"""
        if exception_placement:
            self.text_label.config(text=message)
            self.text_label.place(x=(self.wind_width - self.text_label.winfo_reqwidth()) / 2, y=52)
        else:
            self.text2_label.config(text=message)
            self.text2_label.place(x=(self.wind_width - self.text2_label.winfo_reqwidth()) / 2, y=132)

    def run(self):
        """main loop"""
        self.root.mainloop()
