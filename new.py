import os

def print_subfolders(path, indent="", level=1, max_level=4):
    if level > max_level:
        return

    try:
        items = sorted(os.listdir(path))
    except PermissionError:
        return

    for item in items:
        full_path = os.path.join(path, item)
        if os.path.isdir(full_path):
            print(f"{indent}{item}")
            print_subfolders(full_path, indent + "    ", level + 1, max_level)

if __name__ == "__main__":
    root_path = "."  # current folder
    print_subfolders(root_path, level=1, max_level=4)
