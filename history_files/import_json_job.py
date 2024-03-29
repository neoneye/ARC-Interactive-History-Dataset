import os
import json

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

# These files are generated by the review page on https://braingridgame.com/
# Example of filename: `approved-2024-03-24T14-32-16.json`
def extract_and_save_json_contents(json_content, repo_dir):
    # Parse the JSON content
    data = json.loads(json_content)
    # For each nested JSON string in the 'json' field, extract and save it
    for item in data:
        if 'json' in item:
            nested_json = item['json']
            next_dir, next_file = get_next_name(repo_dir)
            next_dir_path = os.path.join(repo_dir, next_dir)
            if not os.path.exists(next_dir_path):
                os.makedirs(next_dir_path)
            dest_file_path = os.path.join(next_dir_path, next_file)
            with open(dest_file_path, 'w') as file:
                file.write(nested_json)

# Modified move_files_to_repo to handle new file type
def move_files_to_repo(input_dir, repo_dir):
    input_files = [f for f in os.listdir(input_dir) if f.endswith('.json')]
    if not input_files:  # Check if the list is empty
        print("No JSON files found in the input directory.")
        return  # Exit the function if there are no JSON files to process

    for input_file in input_files:
        file_path = os.path.join(input_dir, input_file)
        with open(file_path, 'r') as file:
            content = file.read()
        # Check if the file is of the new type with embedded JSON strings
        if "review" in input_file:
            # Extract and save the embedded JSON strings
            extract_and_save_json_contents(content, repo_dir)
            # Remove the processed file
            os.remove(file_path)
        else:
            next_dir, next_file = get_next_name(repo_dir)
            next_dir_path = os.path.join(repo_dir, next_dir)
            if not os.path.exists(next_dir_path):
                os.makedirs(next_dir_path)
            dest_file = os.path.join(next_dir_path, next_file)
            os.rename(file_path, dest_file)

# Usage example:
input_dir = "import_json"
repo_dir = "."
move_files_to_repo(input_dir, repo_dir)
