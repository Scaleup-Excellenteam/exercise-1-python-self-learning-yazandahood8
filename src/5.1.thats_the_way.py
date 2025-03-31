import os

def thats_the_way(directory: str):
    """
    Returns a list of all files in the given directory that start with 'deep'.
    """
    return [
        file
        for file in os.listdir(directory)
        if file.startswith("deep") and os.path.isfile(os.path.join(directory, file))
    ]

if __name__ == "__main__":
    directory = "images"
    matching_files = thats_the_way(directory)
    print("Files found:", matching_files)
    print("Number of files starting with 'deep':", len(matching_files))
