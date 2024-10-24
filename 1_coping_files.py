import shutil

# Copy a single file from source to destination
source_file = 'example.txt'  # The file you want to copy
destination_file = 'copy_of_example.txt'  # The destination path

# Use shutil.copy() to copy the file
shutil.copy(source_file, destination_file)

print(f"Copied {source_file} to {destination_file}")