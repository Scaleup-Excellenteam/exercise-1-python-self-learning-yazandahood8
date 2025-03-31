import os

def get_files_starting_with_deep(directory: str):
    """
    Returns a list of all files in the given directory that start with 'deep'.
    """
    return [file for file in os.listdir(directory) if file.startswith("deep") and os.path.isfile(os.path.join(directory, file))]

# Test the function with the 'images' directory
if __name__ == "__main__":
    directory = "images"
    matching_files = get_files_starting_with_deep(directory)
    print("Files found:", matching_files)
    print("Number of files starting with 'deep':", len(matching_files))


