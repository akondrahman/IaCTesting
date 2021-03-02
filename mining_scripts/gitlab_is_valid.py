# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 12:55:44 2020

@author: mehedi.md.hasan
"""

import requests, json, pymysql, re, gitlab
from datetime import datetime
db_conn = pymysql.connect("localhost","root","","test", charset='utf8' )
cursor = db_conn.cursor()
gl = gitlab.Gitlab('https://gitlab.com', private_token='ym_J9_F6GBXf4yF2ToQs')



def get_all_gitlab_repo_id():
   
    try:
        cursor.execute('select * from gitlab_repos_puppet where does_repo_exist is null')
        rows = cursor.fetchall()
    except:
        print(Exception)
        rows = []
       
    return rows

def is_valid_repo(project_id):
    try:
        project = gl.projects.get(project_id, as_list=True)
        try:
            project_id_from_api = project.id
            print(f'Project ID {project_id_from_api} exists')
            return 1
        except:
            print(f'Inner Exception')
            err_message = project.message
            print(f'Error is {err_message}')
            return 0
    except Exception as e:
        print(f'Outer Exception for project {project_id}')
        print (e)
        return 0

def update_does_repo_exist_info():
    repos = get_all_gitlab_repo_id()
    print(f'No of repos is: {len(repos)}')
    for repo in repos:
            is_valid = is_valid_repo(repo[0])
            print(f'Updating repo {repo[0]} with is_valid  {is_valid}')
            update_query = 'update gitlab_repos_puppet set does_repo_exist = %s where id = %s'
            val = (is_valid,repo[0])
            cursor.execute(update_query, val)
            db_conn.commit()
            

update_does_repo_exist_info()
#update_fork_info()