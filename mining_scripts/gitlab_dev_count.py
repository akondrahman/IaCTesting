import requests, json, pymysql, re, gitlab
from datetime import datetime
db_conn = pymysql.connect("localhost","root","","test", charset='utf8' )
cursor = db_conn.cursor()
gl = gitlab.Gitlab('https://gitlab.com', private_token='ym_J9_F6GBXf4yF2ToQs')



def get_all_gitlab_repo_id():
   
    try:
        cursor.execute('select * from gitlab_repos where repo_lifetime_in_month>0')
        rows = cursor.fetchall()
    except:
        print(Exception)
        rows = []
       
    return rows


def update_developer_count():
    repos = get_all_gitlab_repo_id()
    print(f'No of repos is: {len(repos)}')
    for repo in repos:
        project = gl.projects.get(repo[0])
        members = project.members.all(all=True)
        try:
            developer_count = len(members)
        except:
            developer_count = 0
        print(f'Updating developer count of repo {repo[0]} with value {developer_count}')
        update_query = "update gitlab_repos set no_of_developers = %s where id = %s"
        val = (developer_count ,repo[0])
        cursor.execute(update_query, val)
        db_conn.commit()
            
update_developer_count()