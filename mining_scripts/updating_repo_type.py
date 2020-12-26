# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 01:27:46 2020

@author: mehedi.md.hasan
"""

import pymysql
import logging
# logging.basicConfig(level=logging.DEBUG,filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s)')


db_conn = pymysql.connect("localhost","root","","test", charset='utf8' )
cursor = db_conn.cursor()


def get_all_github_repo_id():
    
    try:
        cursor.execute('select * from final_repos')
        rows = cursor.fetchall()
    except:
        print(Exception)
        rows = []
        
    return rows

def update_iac_antipatterns(repo_id, project_name, repo_type):
    update_query = 'update iac_anti_patterns_v2 set repo_type = %s, project_name = %s where project_id = %s'
    val = (repo_type, project_name, repo_id)
    try:
        cursor.execute(update_query, val)
        db_conn.commit()
        print(f'Updated repo {project_name}')
    except Exception as e:
        print (e)



repos = get_all_github_repo_id()
base_dir = r"C:\mined_repos"
for repo in repos:
    repo_id = repo[0]
    project_name = repo[1]
    repo_type = repo[13]
    update_iac_antipatterns(repo_id, project_name, repo_type)
