import os

def create_directory(directory_name):
    """
    Creates a new directory.
    Args:
        directory_name (str): Name of the directory to create.
    """
    try:
        os.mkdir(directory_name)
        print(f"Directory '{directory_name}' created successfully.")
    except FileExistsError:
        print(f"Directory '{directory_name}' already exists.")

def write_to_file(file_name, content):
    """
    Writes content to a file.
    Args:
        file_name (str): Name of the file.
        content (str): Text to write to the file.
    """
    with open(file_name, "w") as file:
        file.write(content)
        print(f"Content written to '{file_name}' successfully.")

def read_from_file(file_name):
    """
    Reads content from a file.
    Args:
        file_name (str): Name of the file.
    Returns:
        str: Contents of the file.
    """
    try:
        with open(file_name, "r") as file:
            return file.read()
    except FileNotFoundError:
        return f"File '{file_name}' not found."

def list_files_in_directory(directory_name):
    """
    Lists files in a directory.
    Args:
        directory_name (str): Name of the directory.
    """
    files = os.listdir(directory_name)
    if files:
        print(f"Files in '{directory_name}':")
        for file in files:
            print(file)
    else:
        print(f"No files found in '{directory_name}'.")

# Example usage
directory_name = "my_directory"
create_directory(directory_name)

file_name = "my_file.txt"
content_to_write = "Hello, world!"
write_to_file(file_name, content_to_write)

read_content = read_from_file(file_name)
print(f"Read from '{file_name}': {read_content}")

list_files_in_directory(directory_name)
