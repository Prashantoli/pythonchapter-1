import os

# Specify the directory path
directory_path = "C:/"  # Change this to your directory

# Get the list of all files and directories in the specified directory
contents = os.listdir(directory_path)

# Print the contents
for item in contents:
    print(item)
