import sys
import os
import shutil
import git
from github import Github
user=sys.argv[1]
pwd=sys.argv[2]
g = Github(user, pwd)
drive_path = "G:/我的雲端硬碟/Github/"
print("Start backing up")
for repo in g.get_user().get_repos():
    if repo.private == False:
        if os.path.exists(drive_path+repo.name):
            shutil.rmtree(drive_path+repo.name)
            git.Git(drive_path).clone('https://github.com/Msiciots/'+repo.name+'.git')
        else: 
            git.Git(drive_path).clone('https://github.com/Msiciots/'+repo.name+'.git')
print("Finish!")
# sys.exit()