from jinja2 import Environment, FileSystemLoader

# Define directory values to pass to jinja
downloads_dir = "Downloads"
wallpapers_dynamic_dir = "Wallpapers/Dynamic"
pictures_dir = "Pictures"
documents_dir = "Documents"
videos_dir = "Videos"
music_dir = "Music"

environment = Environment(loader=FileSystemLoader("templates/"))
template = environment.get_template("organize_script.j2")

filename = f"organize_files_1.sh"
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