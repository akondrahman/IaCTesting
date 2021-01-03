# # -*- coding: utf-8 -*-
# """
# Created on Tue Dec  1 01:27:46 2020

# @author: mehedi.md.hasan
# """
from git import Repo
import pymysql
# import logging
# # logging.basicConfig(level=logging.DEBUG,filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s)')


db_conn = pymysql.connect("localhost","root","","test", charset='utf8' )
cursor = db_conn.cursor()


def get_all_github_repo_id():
    
    try:
        cursor.execute('select * from final_repos where id>6000' )
        rows = cursor.fetchall()
    except:
        print(Exception)
        rows = []
        
    return rows

def update_test_commit_summary(repo_id, repo_name, total_commit_count, test_commit_count):
    ins_query = 'insert into test_commit_summary (repo_id, repo_name, total_commits, test_commits) values (%s, %s, %s, %s)'
    val = (repo_id, repo_name, total_commit_count, test_commit_count)
    try:
        cursor.execute(ins_query, val)
        db_conn.commit()
        print(f'Updated repo {repo_name}')
    except Exception as e:
        print (e)



def is_substring( substrings, long_string):
    return substrings in long_string

def find_committer_email(repo_id, repo_name, repo_dir):
    repo = Repo(repo_dir)
    contributors = []
    
    commits = list(repo.iter_commits())

    for commit in commits:
        author = commit.author.email
        if author not in contributors:
            contributors.append(author)
        
    
    return contributors
    


repo_dir = r"C:\Users\mehedi.md.hasan\PythonWorkspace\ostk-ansi\ansible-role-container-registry"
repo_name = "ansible-role-container-registry"
repo_id = 10283

emails = find_committer_email(repo_id, repo_name, repo_dir)
print(emails)

# repos = get_all_github_repo_id()
# base_dir = r"C:\mined_repos"
# for repo in repos:
#     top_dir = repo[1].split("/")[0]
#     project_dir = repo[1].split("/")[1]
#     full_dir = base_dir + "\\" + top_dir + "\\" + project_dir
#     print(full_dir)
#     try:
#         analyze_test_commits(repo[0], project_dir, full_dir)
#     except Exception as e:
#         print(e)
#         continue

    
