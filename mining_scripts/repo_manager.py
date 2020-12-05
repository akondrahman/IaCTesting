# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 23:17:30 2020

@author: mehedi.md.hasan
"""

import pymysql, http.client, os, git, shutil,stat
from os import path
import requests, json
from datetime import datetime


db_conn = pymysql.connect("localhost","root","","test", charset='utf8' )
cursor = db_conn.cursor()
github_conn = http.client.HTTPSConnection("api.github.com")

def get_all_github_repo_id():
    
    try:
        cursor.execute('select * from github_repos')
        rows = cursor.fetchall()
    except:
        print(Exception)
        rows = []
        
    return rows


def update_repo_repo_details(repo, repo_type):
    ext_dir = r'C:\Users\mehedi.md.hasan\PythonWorkspace\mined_repos'
    if repo_type == 1:
        repo_url = "https://github.com/"+repo[1]+"/"
        contributor_count = get_contributor_count(repo[1])
        ansible_percentage = find_iac_percentage(repo[1], ext_dir, repo_type)
        
    elif repo_type == 2:
        repo_url = "https://gitlab.com/"+repo[1]+"/"
    
    update_query = "update github_repos set repo_url = %s, no_of_developers = %s, iac_script_percentage = %s where id = %s"
    val = (repo_url,contributor_count, ansible_percentage, repo[0])
    cursor.execute(update_query, val)
    
    db_conn.commit()


def get_contributor_count(repo_name):
    payload = ''
    headers = {
            'Accept': 'application/vnd.github.v3+json',
            'User-Agent': 'talismanic',
            'Authorization': 'Basic dGFsaXNtYW5pYzphZDM2YzJkMzMxNzg5ZjhhZTdkZmE0ZjQyYzdmODQ3ODhkYmQyYzcx'
            }
    
    endpoint = "https://api.github.com/repos/" + repo_name +"/contributors"
    
#    github_conn.request("GET", endpoint, payload, headers)
    
    
    try:
#        res = github_conn.getresponse()
        
#        res_data = res.read()
        res_data = requests.request("GET", endpoint, headers=headers, data=payload)
        out = json.loads(res_data.text)
        print(f"Contributor count for {repo_name} is {len(out)}")
        return len(out)
    except Exception as e:
        print(e)
        return 0



def download_repo(ext_dir, repo_name, repo_type):
    print(f"starting to download repository {repo_name}")
    print("=================")
    print("Start Time")
    base_repo = repo_name.split("/")[1]
    full_dir = ext_dir+"\\"+base_repo
    if repo_type == 1:
        repo_url = "https://github.com/"+repo_name
        try:
            print(datetime.now())
            git.Git(ext_dir).clone(repo_url)
            print("Download completed")
            print("=================")    
            print(datetime.now())
            return True
        
        except Exception as e:
            print(e)
            if (os.path.exists(full_dir)):
                return True
            else:
                return False
    
def delete_repo(full_dir):
    print(f"deleting the directory: {full_dir}")
    print("=================")
    print(datetime.now())
    for root, dirs, files in os.walk(full_dir):
        for dir in dirs:
            os.chmod(path.join(root, dir), stat.S_IRWXU)
        for file in files:
            os.chmod(path.join(root, file), stat.S_IRWXU)
    
    try:
        shutil.rmtree(full_dir)
        print("deletion completed")
        print("=================")
        print(datetime.now())

    except Exception as e:
        print(e)
        
    

def count_file_type(dir_name, extension ):
    total_file_count = 0
    extension_file_count = 0
    print(f"Counting the {extension} files in repository {dir_name}")
    print("=================")
    for root_, dirnames, filenames in os.walk(dir_name):
        for file_ in filenames:
            full_path_file = os.path.join(root_, file_) 
            if(os.path.exists(full_path_file)):
                total_file_count += 1
                if (file_.endswith(extension))  :
                    extension_file_count += 1
    
    print("Counting completed")                
    print("=================")    
    return total_file_count, extension_file_count



def find_iac_percentage(repo_name, ext_dir, repo_type):

    if download_repo(ext_dir, repo_name, repo_type):
        base_repo = repo_name.split("/")[1]
        full_dir = ext_dir+"\\"+base_repo
        total_files, yml_files = count_file_type(full_dir, ".yml")
        total_files, yaml_files = count_file_type(full_dir, ".yaml")
        ansible_files = yaml_files + yml_files
        if total_files >0:
            percentage = ansible_files/total_files*100
        else:
            percentage = 0
        print(f'Ansible repo percentage maximum {percentage}')
        
        
        delete_repo(full_dir)

        
        return percentage
        

    
#ext_dir = r'C:\Users\mehedi.md.hasan\PythonWorkspace\mined_repos'
#repo_name = 'Talismanic/ansible-examples'
#repo_type = 1
#find_iac_percentage(repo_name, ext_dir, repo_type)
#download_repo(ext_dir, repo_name, repo_type)

#get_contributor_count("zrs233/ursula")
repos = get_all_github_repo_id()

for repo in repos:
    print(repo[6])
    print (f'\n ***Repo ID is {repo[0]} ***\n\n')
    if repo[0]>1193:
        if repo[6] == None or (repo[6] <1 and repo[3] == None):
            update_repo_repo_details(repo, 1)
#
#
#get_contributors("antirez/redis")
#count = 2
#for repo in repos:
#    if count<3:
#        get_contributors(repo[1])
#        count +=1
    
    

