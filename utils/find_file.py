import os


def find_file_by_extension(extension):
    # Get the current directory, then go up two levels
    current_directory = os.path.dirname(os.path.abspath(__file__))
    parent_directory = os.path.abspath(os.path.join(current_directory, '..'))  # Go up two levels
    print(parent_directory)
    # Loop through all files in the parent directory
    for filename in os.listdir(parent_directory):
        if filename.endswith(extension):
            return filename
    return None
# If no file with the specified extension is found
