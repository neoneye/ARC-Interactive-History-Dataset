import subprocess
import os

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
