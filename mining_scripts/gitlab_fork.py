import requests, json, pymysql, re, gitlab
from datetime import datetime
db_conn = pymysql.connect("localhost","root","","test", charset='utf8' )
cursor = db_conn.cursor()
gl = gitlab.Gitlab('https://gitlab.com', private_token='ym_J9_F6GBXf4yF2ToQs')



def get_all_gitlab_repo_id():
   
    try:
        cursor.execute('select * from gitlab_repos where repo_lifetime_in_month>0 and no_of_developers>0 and iac_script_percentage>10')
        rows = cursor.fetchall()
    except:
        print(Exception)
        rows = []
       
    return rows

def is_fork(project_id):
    try:
        project = gl.projects.get(project_id, as_list=True)
        try:
            forked_from = project.forked_from_project
            print(f'Forked from: {forked_from}')
            return 1
        except:
            return 0
    except Exception as e:
        print (e)
        return 0

def update_fork_info():
    repos = get_all_gitlab_repo_id()
    print(f'No of repos is: {len(repos)}')
    for repo in repos:
            is_forked = is_fork(repo[0])
            print(f'Updating repo {repo[0]} with is_clone {is_forked}')
            update_query = 'update gitlab_repos set is_clone = %s where id = %s'
            val = (is_forked,repo[0])
            cursor.execute(update_query, val)
            db_conn.commit()
            


update_fork_info()