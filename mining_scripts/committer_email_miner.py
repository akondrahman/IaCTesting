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
        cursor.execute('select distinct(project_name)  from iac_anti_patterns_v2 where Skip_Ansible_Lint>0 or External_Dependency>0 or Assertion_Roulette>0 or Local_Only_Test >0 or No_ENV_CleanUp>0' )
        rows = cursor.fetchall()
    except:
        print(Exception)
        rows = []
        
    return rows

def update_emails(full_email, email_domain):
    ins_query = 'insert into emails (email, domain) values (%s, %s)'
    val = (full_email, email_domain)
    try:
        cursor.execute(ins_query, val)
        db_conn.commit()
        print(f'Updated email for {full_email}')
    except Exception as e:
        print (e)



# def is_substring( substrings, long_string):
#     return substrings in long_string

def find_committer_email(repo_dir):
    print(repo_dir)
    try:
        repo = Repo(repo_dir)
    except Exception as e:
        print(e)
        pass
    contributors = []
    
    try:
        commits = list(repo.iter_commits())
        for commit in commits:
            author = commit.author.email
            # print(author)
            if author not in contributors:
                email_domain = author.split("@")[1]
                if email_domain != "users.noreply.github.com":
                    try:
                        update_emails(author, email_domain)
                    except Exception as e:
                        print(e)
                        continue


    except Exception as e:
        print (e)
        pass

        
    
    return contributors

def update_contributor_list(repo_dir, repo_name):
    write_file = open("contributors_email.txt", "a+")
    try:
        emails = find_committer_email(repo_dir)
        # print(emails)
        if len(emails)>0:
            write_file.write("Repository Name: %s\n"%repo_name)
            write_file.write("Contributor List %s\n"%emails)
    except Exception as e:
        print(e)
        pass



# repo_dir = r"C:\Users\mehedi.md.hasan\PythonWorkspace\ostk-ansi\ansible-role-container-registry"
# repo_name = "ansible-role-container-registry"
# repo_id = 10283

# emails = find_committer_email(repo_id, repo_name, repo_dir)
# print(emails)

repos = get_all_github_repo_id()
base_dir = r"C:\mined_repos-orig"
repo_list = []
for repo in repos:

    if not repo[0] in repo_list:
        repo_list.append(repo[0])
        print(repo[0])
        top_dir = repo[0].split("/")[0]
        project_dir = repo[0].split("/")[1]
        full_dir = base_dir + "\\" + top_dir + "\\" + project_dir
        print(full_dir)
        try:
            update_contributor_list(full_dir, project_dir)
        except Exception as e:
            # print(e)
            continue

    
