import os
import json

# Path to the dataset repository
repo_path = '.'

# Function to check if a file should be deleted
def should_delete_file(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
        if data["summary"]["test unsolved count"] >= 1:
            return True
    return False

# Function to delete files
def delete_files(directory):
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if filename.endswith('.json') and should_delete_file(file_path):
            print(f"Deleting {file_path}...")
            os.remove(file_path)

# Loop through all directories in the repo
for subdir in os.listdir(repo_path):
    subdir_path = os.path.join(repo_path, subdir)
    if os.path.isdir(subdir_path):
        delete_files(subdir_path)

print("Completed checking and removing files.")

# regenerate directory_content.json
os.system('python3 directory_content_generate.py')
