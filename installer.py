import tkinter as tk
from tkinter import filedialog
import shutil
import os
from tkinter import messagebox
import getpass

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Minecraft Mod Installer for Danielzimiao's Server")
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.greeting = tk.Label(self, text="Welcome to the Minecraft Mod Installer for Danielzimiao's Server!")
        self.greeting.pack(side="top")

        self.select_button = tk.Button(self)
        self.select_button["text"] = "Select Directory"
        self.select_button["command"] = self.select_directory
        self.select_button.pack(side="top")

    def select_directory(self):
        if sys.platform == "win32":  # If the operating system is Windows
            username = getpass.getuser()
            minecraft_mods_dir = f"C:\\Users\\{username}\\AppData\\Roaming\\.minecraft\\mods"
            if os.path.exists(minecraft_mods_dir):
                use_minecraft_mods_dir = messagebox.askyesno(
                    "Minecraft Mods Directory Found",
                    f"The directory {minecraft_mods_dir} exists. Do you want to place the files in this directory?"
                )
                if use_minecraft_mods_dir:
                    self.move_files_to_directory(minecraft_mods_dir)
                    return

        # If the operating system is not Windows, or the .minecraft/mods directory doesn't exist,
        # or the user chose not to use the .minecraft/mods directory, ask the user to select a directory.
        directory = filedialog.askdirectory()
        if directory:  # A directory was selected
            self.move_files_to_directory(directory)

    def move_files_to_directory(self, directory):
        base_folder = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
        source_folder = os.path.join(base_folder, 'mods')
        if not os.path.exists(source_folder):
            os.makedirs(source_folder)
        moved_files = []
        for file_name in os.listdir(source_folder):
            source_file = os.path.join(source_folder, file_name)
            destination_file = os.path.join(directory, file_name)
            if not os.path.exists(destination_file):
                shutil.move(source_file, destination_file)
                moved_files.append(file_name)
            else:
                print(f"File {file_name} already exists in the destination directory.")
        self.show_moved_files(moved_files)

    def show_moved_files(self, moved_files):
        moved_files_label = tk.Label(self, text="Moved files: " + ", ".join(moved_files))
        moved_files_label.pack(side="top")
        self.exit_button = tk.Button(self)
        self.exit_button["text"] = "Exit"
        self.exit_button["command"] = self.master.destroy
        self.exit_button.pack(side="top")

def main():
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()

if __name__ == "__main__":
    main()