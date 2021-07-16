import re
from sys import float_repr_style
from git import Repo
import pymysql
import os, re
db_conn = pymysql.connect(host='localhost',
                      user='root',
                      password='',
                      database='test',
                      charset='utf8')
cursor = db_conn.cursor()


# def clean_up(string):
#     return re.sub('[^A-Za-z0-9. ]+\"', ' ', string)

def fetch_project_names():
    try:
        cursor.execute('select distinct project_name from commit_messages where bugflag = 1 and bug_script_type <1 and loc_added is null')
        # cursor.execute('select distinct project_name from iac_anti_patterns_v2 where repo_type=1  limit 5')
        # select_query = """select distinct project_name from commit_messages where bugflag = bugflag limit 1"""
        # cursor.execute(select_query, (bugflag) )
        rows = cursor.fetchall()
        final_result = [i[0] for i in rows]
        # print("rows: " ,rows)
    except:
        print(Exception)
        final_result = []
        
    return final_result

def find_all_hashes(project):
    select_query = """select commit_hash from commit_messages where bugflag = 1 and project_name = %s"""
    try:
        cursor.execute(select_query, (project) )
        rows = cursor.fetchall()
        final_result = [i[0] for i in rows]
        # print("rows: " ,rows)
    except:
        print(Exception)
        final_result = []
        
    return final_result


def find_repo_dir(repo_name):

    ext_dir = r'C:\\mined_repos'
    
    base_repo = repo_name.split("/")[0]

    full_dir = ext_dir+"\\"+base_repo
    return os.path.join(full_dir, repo_name.split("/")[1])

def update_loc_info(project, commit_hash, file_name, loc_added, loc_deleted):
    upd_query = 'update commit_messages set loc_added = %s, loc_deleted = %s where (project_name = %s and commit_hash = %s and file_name like %s)'
    val = (int(loc_added), int(loc_deleted), project, commit_hash, str('%'+file_name))
    try:
        # print(ins_query)
        cursor.execute(upd_query, val)
        # print(upd_query)
        db_conn.commit()
        # print(f'Updated repo: {project} ')
    except Exception as e:

        print ("Exception while update: ", e)



def commit_diff_dumper():
    projects = fetch_project_names()

    for project in projects:
        repo_path = find_repo_dir(project)
        hashes = find_all_hashes(project) 
        print("repo path: ", repo_path)
        repo = Repo(repo_path)
        the_git = repo.git
        log = the_git.log('--since=2013-09-01', '--numstat')
        # print("log: ", log)
        in_hashes = False
        for line in log.split('\n'):
            
            if line.startswith('commit'):
                commit = line.split(' ')[1]
                if commit in hashes:
                    in_hashes = True

                    print("Found in hashes: ", commit)
                else:
                    in_hashes = False
                # print("commit: ", commit)
            if line.startswith('Author') or line.startswith('Merge') or line.startswith('Date') or line.startswith(' ') or line.startswith('\n') or len(line)<1:
                continue

            else:
                # print(line)
                summary = re.match(r"(\d+)\s+(\d+)\s+(.+)", line)
                # print("summary: ", summary)
                if summary :
                    file_name = summary[3]
                    loc_added = summary[1]
                    loc_deleted = summary[2]

                    # print("project name: ", project, "Commit: ", commit, " FileName: ", file_name, " Added: ", loc_added, " Deleted: ", loc_deleted)

                    if in_hashes:
                        print("project name: ", project, "Commit: ", commit, " FileName: ", file_name, " Added: ", loc_added, " Deleted: ", loc_deleted)
                        file_name = file_name.split('/')
                        file_name_len = len(file_name)
                        file_name = file_name[file_name_len -1]

                        update_loc_info(project, commit, file_name, loc_added, loc_deleted)



commit_diff_dumper()