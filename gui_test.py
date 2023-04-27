import os
import tkinter as tk
from tkinter import ttk
from tkinter import Entry, Label
from jinja2 import Environment, FileSystemLoader

# Create bash script based on inputs
def generate_script():

    # Read in values
    downloads_dir = str(downloads_field.get())
    wallpapers_dynamic_dir = str(wallpapers_field.get())
    documents_dir = str(documents_field.get())

    # Define jinja template to use
    environment = Environment(loader=FileSystemLoader("templates/"))
    template = environment.get_template("organize_script.j2")

    # Create shell script from template and directory values
    filename = f"organize_files.sh"
    content = template.render(
        downloads_dir=downloads_dir,
        wallpapers_dynamic_dir=wallpapers_dynamic_dir,
        documents_dir=documents_dir,
    )
    with open(filename, mode="w", encoding="utf-8") as writer:
        writer.write(content)

    # Make shell script executable
    os.system("chmod +x organize_files.sh")


# Create TKinter window and set size
win = tk.Tk()
win.geometry("800x600")

# Add Title and prompts for file paths
win.title("File Organizer")
Label(win, text="Please provide your Downloads folder path: ").place(x=5, y=10)
downloads_field = Entry(win, width=40)
downloads_field.place(x=320, y=10)
Label(win, text="Please provide your Wallpaper folder path: ").place(x=5, y=50)
wallpapers_field = Entry(win, width=40)
wallpapers_field.place(x=320, y=50)
Label(win, text="Please provide your Documents folder path: ").place(x=5, y=90)
documents_field = Entry(win, width=40)
documents_field.place(x=320, y=90)
ttk.Button(win, text="Generate", command=generate_script).place(x=340, y=120)

# Start main loop
win.mainloop()