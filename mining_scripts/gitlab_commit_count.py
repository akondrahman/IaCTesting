import requests, json, pymysql, re, gitlab
from datetime import datetime
db_conn = pymysql.connect("localhost","root","","test", charset='utf8' )
cursor = db_conn.cursor()
gl = gitlab.Gitlab('https://gitlab.com', private_token='ym_J9_F6GBXf4yF2ToQs')



def get_all_gitlab_repo_id():
   
    try:
        cursor.execute('select id, repo_lifetime_in_month from gitlab_repos_puppet where repo_lifetime_in_month>0 and no_of_developers>0')
        rows = cursor.fetchall()
    except:
        print(Exception)
        rows = []
       
    return rows


def find_gitlab_commit_count(project_id, per_page, page_no):
    try:
        project = gl.projects.get(project_id)
    # print(project)
        commits = project.commits.list(per_page = per_page, page = page_no)
            
    # print(len(commits))
        return len(commits)
    except:
        return 0

def calculate_total_commit(project_id):
    
    total_commit_count = 0
        
    for i in range(1,4):
        per_page = 20
        page_no = i
        current_commit_count = find_gitlab_commit_count(project_id, per_page, page_no)
        total_commit_count +=current_commit_count

        if current_commit_count < per_page:
            print(f'Reached on final page : {i} and total commit count is :{total_commit_count}')
            return total_commit_count
    
    return total_commit_count
    

def update_total_commits_n_frequency():
    repos = get_all_gitlab_repo_id()
    print(f'No of repos is: {len(repos)}')
    for repo in repos:
            total_commit_count = calculate_total_commit(repo[0])
            if repo[1] > 0:
                monthly_commit_frequency = int(total_commit_count/repo[1])
            else:
                monthly_commit_frequency = total_commit_count

            print(f'Updating repo {repo[0]} with total commit {total_commit_count} and monthly commit frequency as {monthly_commit_frequency}')
            update_query = 'update gitlab_repos_puppet set total_commits = %s, monthly_commit_frequency = %s where id = %s'
            val = (total_commit_count,monthly_commit_frequency ,repo[0])
            cursor.execute(update_query, val)
            db_conn.commit()
        


update_total_commits_n_frequency()