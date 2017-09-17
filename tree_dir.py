import os

# Setup
cwd = os.getcwd()
ignore = ["Source", "src", "bin", "Builds", "build", "lib",
            "Library", "target", "project"]


def directory_stack(current_dir, stack, indent):
    if(os.path.isdir(current_dir)):
        valid_dirs = [d for d in os.listdir(current_dir) if d not in ignore and not d.startswith(".")]

        for dirs in valid_dirs:
            stack.insert(0, dirs)
            next_dir = current_dir + "/" + dirs
            # Print output
            print(indent + " | " + dirs + "\n")
            indent += "  "
            # Recursive call to next level
            directory_stack(next_dir, stack, indent)


# Get list of children
dir_stack = []

directory_stack(cwd, dir_stack, "")
