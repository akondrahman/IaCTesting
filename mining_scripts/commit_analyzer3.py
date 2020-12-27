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
        cursor.execute('select * from final_repos where id>4899' )
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

def analyze_test_commits(repo_id, repo_name, repo_dir):
    repo = Repo(repo_dir)
    total_commit_count = 0
    test_commit_count = 0
    test_commit_hashes = []
    for commit in list(repo.iter_commits()):
        total_commit_count +=1
        # print(commit)
        # print(commit.stats.files)
        changed_files = commit.stats.files
        for ch_file in changed_files:
            is_test = is_substring(".yml", ch_file) or  is_substring(".yaml", ch_file)
                   

            if is_test == True:
                # print (f'Changed files are: {ch_file}')
                test_commit_hashes.append(commit)
                test_commit_count +=1
                break

    print(f'test commit hashes are {test_commit_hashes}')
    print(f'total test related commits {test_commit_count}')
    print(f'total commits {total_commit_count}')
    update_test_commit_summary(repo_id, repo_name, total_commit_count, test_commit_count)


repos = get_all_github_repo_id()
base_dir = r"C:\mined_repos"
for repo in repos:
    top_dir = repo[1].split("/")[0]
    project_dir = repo[1].split("/")[1]
    full_dir = base_dir + "\\" + top_dir + "\\" + project_dir
    print(full_dir)
    try:
        analyze_test_commits(repo[0], project_dir, full_dir)
    except Exception as e:
        print(e)
        continue

    
