import os
from jinja2 import Environment, FileSystemLoader

## WHAT DOES THIS DO ##
## DIRECTIONS ##


# Grab directory values from command line
downloads_dir = str(input(f"Provide Download Folder: "))
wallpapers_dynamic_dir = str(input(("Provide Wallpaper Folder: ")))
pictures_dir = str(input("Provide Picture Folder: "))
documents_dir = str(input("Provide Document Folder: "))
videos_dir = str(input("Provide Video Folder: "))
music_dir = str(input("Provide Music Folder: "))

# Define jinja template to use
environment = Environment(loader=FileSystemLoader("templates/"))
template = environment.get_template("organize_script.j2")

# Create shell script from template and directory values
filename = f"organize_files.sh"
content = template.render(
    downloads_dir=downloads_dir,
    wallpapers_dynamic_dir=wallpapers_dynamic_dir,
    pictures_dir=pictures_dir,
    documents_dir=documents_dir,
    videos_dir=videos_dir,
    music_dir=music_dir
)
with open(filename, mode="w", encoding="utf-8") as writer:
    writer.write(content)

# Make shell script executable
os.system("chmod +x organize_files.sh")