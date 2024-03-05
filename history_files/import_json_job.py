import os

# Function to get the next directory and file name
def get_next_name(repo_dir):
    last_dir = sorted([d for d in os.listdir(repo_dir) if d.isdigit()], key=int)[-1]
    last_dir_path = os.path.join(repo_dir, last_dir)
    files = sorted([f for f in os.listdir(last_dir_path) if f.endswith('.json')], key=lambda x: int(x.split('.')[0]))
    if len(files) < 100:
        next_dir = last_dir
        next_file = f"{len(files):02}.json"
    else:
        next_dir = str(int(last_dir) + 1)
        next_file = "00.json"
    return next_dir, next_file

# Move files to the repo, renaming and creating directories as necessary
def move_files_to_repo(input_dir, repo_dir):
    input_files = [f for f in os.listdir(input_dir) if f.endswith('.json')]
    if not input_files:  # Check if the list is empty
        print("No JSON files found in the input directory.")
        return  # Exit the function if there are no JSON files to process

    for input_file in input_files:
        next_dir, next_file = get_next_name(repo_dir)
        next_dir_path = os.path.join(repo_dir, next_dir)
        if not os.path.exists(next_dir_path):
            os.makedirs(next_dir_path)
        source_file = os.path.join(input_dir, input_file)
        dest_file = os.path.join(next_dir_path, next_file)
        os.rename(source_file, dest_file)

# Usage example:
input_dir = "import_json"
repo_dir = "."
move_files_to_repo(input_dir, repo_dir)
