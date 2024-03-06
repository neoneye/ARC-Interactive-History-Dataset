import os

# run import_json_job
os.system('python3 import_json_job.py')

# regenerate directory_content.json
os.system('python3 directory_content_generate.py')

# add new files to git
os.system('git add .')

# commit changes
os.system('git commit -m "auto commit"')

# push changes
os.system('git push origin main')
