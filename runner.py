# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 01:27:46 2020

@author: mehedi.md.hasan
"""

import main

import pymysql
import logging
logging.basicConfig(level=logging.DEBUG,filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s)')


db_conn = pymysql.connect("localhost","root","","test", charset='utf8' )
cursor = db_conn.cursor()

#not fo openstack
def get_all_github_repo_id():
    
    try:
        cursor.execute('select * from final_repos')
        rows = cursor.fetchall()
    except:
        print(Exception)
        rows = []
        
    return rows

repos = get_all_github_repo_id()
base_dir = r"C:\mined_repos"
# base_dir = r"C:\Users\mehedi.md.hasan\PythonWorkspace\ostk-ansi\open-stack-new-repos"
for repo in repos:
    top_dir = repo[1].split("/")[0]
    project_dir = repo[1].split("/")[1]
    full_dir = base_dir+"\\"+top_dir+"\\"+project_dir
    # full_dir = base_dir+"\\"+project_dir
    project_name = top_dir+"_"+project_dir
#    project_name = str(repo[0])
#    print(f'full directory is {full_dir}')
#    print(project_name)
    
    
    try:
        main.main(full_dir, project_name)
        logging.debug("repoid %s done", repo[0],)

    except:
        logging.error("repoid %s failed", repo[0],)

        continue
