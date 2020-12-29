# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 00:47:47 2020

@author: mehedi.md.hasan
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 01:27:46 2020

@author: mehedi.md.hasan
"""

import pymysql
#import logging
# logging.basicConfig(level=logging.DEBUG,filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s)')


db_conn = pymysql.connect("localhost","root","","test", charset='utf8' )
cursor = db_conn.cursor()


def get_all_github_repo_id():
    
    try:
        cursor.execute('select distinct project_name from iac_anti_patterns_v2 where repo_type=1 and (No_ENV_CleanUp>0  or Local_Only_Test >0 or Assertion_Roulette>0 or External_Dependency >0 or Skip_Ansible_Lint>0)')
        rows = cursor.fetchall()
    except:
        print(Exception)
        rows = []
        
    return rows

def get_NEC(project_name):
    try:
        select_query ='select file_name from iac_anti_patterns_v2 where project_name=%s and No_ENV_CleanUp>0'
        cursor.execute(select_query, (project_name,))
        rows = cursor.fetchall()
    except Exception as e:
        print(e)
        rows = []
       
    return rows


def get_AR(project_name):
    try:
        select_query ='select file_name from iac_anti_patterns_v2 where project_name=%s and Assertion_Roulette>0'
        cursor.execute(select_query, (project_name,))
        rows = cursor.fetchall()
    except Exception as e:
        print(e)
        rows = []
       
    return rows


def get_LOT(project_name):
    try:
        select_query ='select file_name from iac_anti_patterns_v2 where project_name=%s and Local_Only_Test>0'
        cursor.execute(select_query, (project_name,))
        rows = cursor.fetchall()
    except Exception as e:
        print(e)
        rows = []
       
    return rows


def get_ED(project_name):
    try:
        select_query ='select file_name from iac_anti_patterns_v2 where project_name=%s and External_Dependency>0'
        cursor.execute(select_query, (project_name,))
        rows = cursor.fetchall()
    except Exception as e:
        print(e)
        rows = []
       
    return rows


def get_SAL(project_name):
    try:
        select_query ='select file_name from iac_anti_patterns_v2 where project_name=%s and Skip_Ansible_Lint>0'
        cursor.execute(select_query, (project_name,))
        rows = cursor.fetchall()
    except Exception as e:
        print(e)
        rows = []
       
    return rows


def get_project_meta(project_name):
    try:
        select_query ='select repo_url from final_repos where repo_name=%s and last_commit_date>"2019-12-31"'
        cursor.execute(select_query, (project_name,))
        rows = cursor.fetchall()
    except Exception as e:
        print(e)
        rows = []
       
    return rows


repos = get_all_github_repo_id()
write_file = open("repo_list.txt", "a+")
total_instance = 0    
#print(repos)
for repo in repos:
    project_name = repo[0]
        
    try:
        repo_url = get_project_meta(project_name)[0][0]
        files_SAL = get_SAL(project_name)
        files_ED = get_ED(project_name)
        files_LOT = get_LOT(project_name)
        files_NEC = get_NEC(project_name)
        files_AR = get_ED(project_name)
    
        files_SAL_arr = []
        files_LOT_arr = []
        files_AR_arr = []
        files_NEC_arr = []
        files_ED_arr = []
        write_file.write("\n=========***=========\n")
        write_file.write("%s has repo url as %s\n"%(project_name, repo_url) )
        
        if len(files_SAL) >0:
            write_file.write("This repository has Skip_Ansible_Lint testing anti-patterns in the following files\n")
            for file_SAL in files_SAL:
                write_file.write("%s\n"%file_SAL)
                total_instance += 1
            
            
        if len(files_NEC)>0:
            write_file.write("\nThis repository has No_Environment_CleanUp testing anti-patterns in the following files\n")
            for file_NEC in files_NEC:
                write_file.write("%s\n"%file_NEC)
                total_instance += 1
    
        if len(files_LOT)>0:
            write_file.write("\nThis repository has Local_Only_Test testing anti-patterns in the following files\n")
            for file_LOT in files_LOT:
                write_file.write("%s\n"%file_LOT)
                total_instance += 1
    
        if len(files_AR)>0:
            write_file.write("\nThis repository has Assertion_Roulette testing anti-patterns in the following files\n")
            for file_AR in files_AR:
                write_file.write("%s\n"%file_AR)
                total_instance += 1
    
        if len(files_ED)>0:
            write_file.write("\nThis repository has External_Dependency testing anti-patterns in the following files\n")
            for file_ED in files_ED:
                write_file.write("%s\n"%file_ED)
                total_instance += 1
            
        if total_instance > 200:
            break
    
    except:
        continue
    

write_file.close()