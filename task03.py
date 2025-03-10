import sys
from pathlib import Path
from colorama import Fore

def print_directory_structure(directory: Path, prefix=""):
    """
    Recursively prints the directory structure starting from the given directory.

    Args:
        directory (Path): The directory path to start printing the structure from.
        prefix (str): The prefix string used for formatting the directory structure.
    """
    if not directory.is_dir():
        print(Fore.RED + "Error: The specified path is not a directory.")
        return

    items = sorted(directory.iterdir(), key=lambda x: (not x.is_dir(), x.name.lower()))  

    for index, item in enumerate(items):
        connector = "└── " if index == len(items) - 1 else "├── "
        if item.is_dir():
            print(Fore.BLUE + prefix + connector + "📂 " + item.name + '/')
            print_directory_structure(item, prefix + ("    " if index == len(items) - 1 else "│   "))  
        else:
            print(Fore.GREEN + prefix + connector + "📜 " + item.name)
            

if __name__ == "__main__":
    """
    The main entry point of the script. Validates the command-line arguments and
    initiates the directory structure printing.
    """
    if len(sys.argv) != 2:
        print(Fore.RED + "Use: python3 task03.py /path/to/directory")
        sys.exit(1)

    path = Path(sys.argv[1])

    if not path.exists():
        print(Fore.RED + f"Error: Path '{path}' not found.")
        sys.exit(1)

    print(Fore.YELLOW + f"📦 {path.resolve().name}"+ '/')  
    print_directory_structure(path)



# Usage: python3 task03.py /path/to/directory

# Example: python3 task03.py /Users/olehfedorchuk/Documents/GitHabNeovesrity/python/goit-pycore-hw-04/picture
# Output:
#     📦 picture/
# ├── 📂 Logo/
# │   ├── 📜 IBM+Logo.png
# │   ├── 📜 ibm.svg
# │   └── 📜 logo-tm.png
# ├── 📜 bot-icon.png
# ├── 📜 mongodb.jpg
# └── 📜 requirements.txt