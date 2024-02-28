import os
import json
from datetime import datetime

# Set the path to current directory, or specify an absolute path
repo_path = '.'

def generate_file_structure(repo_path):
    file_structure = {}
    for root, dirs, files in os.walk(repo_path):
        for file in files:
            if file.endswith('.json'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    try:
                        content = json.load(f)
                        dataset = content.get('dataset')
                        task = content.get('task')
                        if dataset and task:
                            # Use the relative file path from the repo's root directory
                            relative_path = os.path.relpath(file_path, repo_path).replace('\\', '/')
                            # Update the file structure dictionary
                            if dataset not in file_structure:
                                file_structure[dataset] = {}
                            if task not in file_structure[dataset]:
                                file_structure[dataset][task] = []
                            file_structure[dataset][task].append(relative_path)
                    except json.JSONDecodeError as e:
                        print(f"Error decoding JSON from {file_path}: {e}")

    # Sort the file structure
    sorted_file_structure = {dataset: {task: sorted(urls) for task, urls in sorted(tasks.items())} for dataset, tasks in sorted(file_structure.items())}

    return sorted_file_structure

# Generate the directory content structure
directory_content = generate_file_structure(repo_path)

# Get the current UTC timestamp
current_timestamp = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%SZ')

# Add the timestamp to the directory content at the top level
directory_content["generatedOn"] = current_timestamp

# Write the structure to a JSON file
with open('directory_content.json', 'w', encoding='utf-8') as f:
    json.dump(directory_content, f, indent=2, ensure_ascii=False)

print("directory_content.json has been generated successfully.")
