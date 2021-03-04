# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 23:27:09 2021

@author: mehedi.md.hasan
"""

import pymysql
import requests, json
#set GIT_PYTHON_GIT_EXECUTABLE=C:\Program Files\Git\cmd\git.exe
db_conn = pymysql.connect("localhost","root","","test", charset='utf8' )
cursor = db_conn.cursor()
#github_conn = http.client.HTTPSConnection("api.github.com")

def get_all_github_repo_id():
   
    try:
        cursor.execute('select * from github_repos_puppet where id>5')
        rows = cursor.fetchall()
    except:
        print(Exception)
        rows = []
       
    return rows


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
        print(f"Contributor count for {repo_name}  is {len(out)}")
        return len(out)
    except Exception as e:
        print(e)
        return 0

def update_dev_count(repo):
    repo_url = "https://github.com/"+repo[1]+"/"
    contributor_count = get_contributor_count(repo[1])
        
    update_query = "update github_repos_puppet set repo_url = %s, no_of_developers = %s where id = %s"
    val = (repo_url,contributor_count, repo[0])
    cursor.execute(update_query, val)
   
    db_conn.commit()


   


repos = get_all_github_repo_id()

for repo in repos:
#    print(repo[6])
#    print (f'\n ***Repo ID is {repo[0]} ***\n\n')
#    if repo[0]>1126 and repo[0]<1450:
    update_dev_count(repo)
#
#
#get_contributors("antirez/redis")
#count = 2
#for repo in repos:
#    if count<3:
#        get_contributors(repo[1])
#        count +=1