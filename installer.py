import tkinter as tk
from tkinter import filedialog
import shutil
import os
import sys
from tkinter import messagebox
import getpass
import ctypes


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Minecraft Mod Installer for Danielzimiao's Server")
        # Set window size
        self.master.geometry("720x540")

        # Center window on screen
        window_width = self.master.winfo_screenwidth()
        window_height = self.master.winfo_screenheight()
        position_right = int(window_width / 2 - 720 / 2)
        position_down = int(window_height / 2 - 540 / 2)
        self.master.geometry("+{}+{}".format(position_right, position_down))

        self.pack(expand=True)
        self.create_widgets()

    def create_widgets(self):
        self.greeting = tk.Label(self, text="Welcome to the Minecraft Mod Installer for Danielzimiao's Server!")
        self.greeting.pack(side="top", anchor="center")

        self.select_button = tk.Button(self)
        self.select_button["text"] = "Select Directory"
        self.select_button["command"] = self.select_directory
        self.select_button.pack(side="top", anchor="center")

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
        messages = []
        for file_name in os.listdir(source_folder):
            source_file = os.path.join(source_folder, file_name)
            destination_file = os.path.join(directory, file_name)
            if not os.path.exists(destination_file):
                shutil.copy2(source_file, destination_file)
                moved_files.append(file_name)
                messages.append(f"File {file_name} copied to the destination directory.")
            else:
                messages.append(f"File {file_name} already exists in the destination directory.")
        self.show_moved_files(moved_files, messages)

    def show_moved_files(self, moved_files, messages):
        for file in moved_files:
            moved_file_label = tk.Label(self, text="Installed Mod: " + file)
            moved_file_label.pack(side="top")
        # for message in messages:
        #     message_label = tk.Label(self, text=message)
        #     message_label.pack(side="top")
        finished_label = tk.Label(self, text="Finished")
        finished_label.pack(side="top")
        self.exit_button = tk.Button(self)
        self.exit_button["text"] = "Exit"
        self.exit_button["command"] = self.master.destroy
        self.exit_button.pack(side="top")

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def main():
    if not True:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
    else:
        root = tk.Tk()
        app = Application(master=root)
        app.mainloop()

if __name__ == "__main__":
    main()