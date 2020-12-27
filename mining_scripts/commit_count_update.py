# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 01:27:46 2020

@author: mehedi.md.hasan
"""

import pymysql
# import logging
# logging.basicConfig(level=logging.DEBUG,filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s)')


db_conn = pymysql.connect("localhost","root","","test", charset='utf8' )
cursor = db_conn.cursor()


def get_all_github_repo_id():
    
    try:
        cursor.execute('select * from test_commit_summary')
        rows = cursor.fetchall()
    except:
        print(Exception)
        rows = []
        
    return rows

def update_iac_commit_count(repo_id, iac_commit_count):
    update_query = 'update final_repos set total_commits = %s where id = %s'
    val = (iac_commit_count, repo_id)
    try:
        cursor.execute(update_query, val)
        db_conn.commit()
        print(f'Updated repo {repo_id} ')
    except Exception as e:
        print (e)



repos = get_all_github_repo_id()
print (len(repos))
# base_dir = r"C:\mined_repos"
for repo in repos:
    repo_id = repo[1]
    # iac_commit_count = repo[4]
    total_commit_count = repo[3]
    update_iac_commit_count(repo_id, total_commit_count)
