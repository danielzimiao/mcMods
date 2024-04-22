from cx_Freeze import setup, Executable

setup(
    name = "installer",
    version = "0.1",
    description = "My application",
    executables = [Executable("installer.py")]
)