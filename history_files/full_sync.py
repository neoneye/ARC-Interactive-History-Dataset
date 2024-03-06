import subprocess
import os

# Make sure current working directory is the directory of this script
cwd_before = os.getcwd()
print("Current working directory, before:", cwd_before)

# Change working directory to the directory of this script
this_script_path = os.path.realpath(__file__)
os.chdir(os.path.dirname(this_script_path))

cwd_after = os.getcwd()
print("Current working directory, after:", cwd_after)

# run import_json_job
os.system('python3 import_json_job.py')

# Run git status --porcelain and capture its output
result = subprocess.run(['git', 'status', '--porcelain'], stdout=subprocess.PIPE, text=True)

# Check if the output is empty
if result.stdout == "":
    print("No changes to commit")
    exit()

print("There are changes to commit")

# regenerate directory_content.json
os.system('python3 directory_content_generate.py')

# add new files to git
os.system('git add .')

# commit changes
os.system('git commit -m "auto commit"')

# push changes
os.system('git push origin main')
