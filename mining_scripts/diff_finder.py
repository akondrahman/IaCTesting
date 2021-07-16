from typing_extensions import final
from git import Repo, RemoteProgress, exc
import pymysql
import os, git, re


class CloneProgress(RemoteProgress):
    def update(self, op_code, cur_count, max_count=None, message=''):
        if message:
            print(message)



# Database Connection
db_conn = pymysql.connect(host='localhost',
                      user='root',
                      password='',
                      database='test',
                      charset='utf8')
cursor = db_conn.cursor()

# File Name
# FILE_NAME = 'dump_commit_diffs.txt'
# FILE_NAME = 'dump_commit_diffs_v2.txt'
FILE_NAME = 'dump_commit_diffs_v3.txt'

keywords = [" error ", " bug ", " fix ", " issue ", " mistake ", " incorrect ", " fault ", " defect " , " flaw ", ]


# repo_path = r'C:\Personal\Research\mollie-api-php'
# file_path = r'C:\Personal\Research\mollie-api-php\src\Resources\MethodCollection.php'
# repo = Repo(repo_path)
repo_type = 1
not_found_repo = 0
not_found_file = 0


def fetch_project_names():
    try:
        cursor.execute('select distinct project_name from commit_messages where bugflag = 1 and bug_script_type = -1')
        # cursor.execute('select distinct project_name from iac_anti_patterns_v2 where repo_type=1  limit 5')
        # select_query = """select distinct project_name from commit_messages where bugflag = bugflag limit 1"""
        # cursor.execute(select_query, (bugflag) )
        rows = cursor.fetchall()
        final_result = [i[0] for i in rows]
    except:
        print(Exception)
        final_result = []
        
    return final_result

def fetch_commit_hash(project, bugflag):
    try:
        select_query = """select distinct commit_hash from commit_messages where project_name= %s and bugflag = %s and bug_script_type=-1"""
        cursor.execute(select_query, (project,bugflag))
        rows = cursor.fetchall()

        final_result = [i[0] for i in rows]
    except:
        print(Exception)
        final_result = []
        
    return final_result


def fetch_test_files(project):
    try:
        select_query = """select file_name from iac_anti_patterns_v2 where project_name=%s"""
        cursor.execute(select_query, (project,))
        rows = cursor.fetchall()
    except:
        print(Exception)
        rows = []
        
    return rows

def write_to_file(header, string):
    with open(FILE_NAME, 'a+') as file_append:
            file_append.write("===========" + header + "==========="+"\n")
            file_append.write(string+"\n")
            
def insert_commit_messages(project_name, repo_path, file_name, commit_hash, commit_message, bugflag):
    ins_query = 'insert into commit_messages (project_name, repo_path, file_name, commit_hash, commit_message, bugflag, repo_type) values (%s, %s, %s, %s, %s, %s, %s)'
    val = (project_name, repo_path, file_name, commit_hash, commit_message, bugflag, repo_type)
    try:
        # print(ins_query)
        cursor.execute(ins_query, val)
        db_conn.commit()
        # print(f'Updated repo {project_name}')
    except Exception as e:
        print (e)


def find_repo_dir(repo_name):

    ext_dir = r'C:\mined_repos'
    
    base_repo = repo_name.split("/")[0]

    full_dir = ext_dir+"\\"+base_repo
    return os.path.join(full_dir, repo_name.split("/")[1])

    # if os.path.exists(full_dir):
    #     return os.path.join(full_dir, repo_name.split("/")[1])
    # else :
    #     os.makedirs(full_dir)
    
    print(full_dir)
    # return full_dir
    
    
#     repo_url = "https://github.com/"+repo_name
#     # repo_url = "https://gitlab.com/"+repo_name
#     try:
#         print(f"starting to download repository {repo_name}")
#         print("=================")
#         git.Git(full_dir).clone(repo_url)
#         print("Download completed")
#         print("=================")    
#         return full_dir+"//"+repo_name.split("/")[1]
       
#     except Exception as e:
#         print(e)
#         return full_dir+"//"+repo_name.split("/")[1]


def file_finder_v2(hashes, repo_path):
    repo = Repo(repo_path)

    for hash in hashes:
        print("hashes: ", hash)
        write_to_file("HASH: ", hash)
        file_names = repo.git.show("--pretty=", "--name-only", hash)
        file_names = file_names.split("\n")
        # print("file names:", file_names)
        for file_name in file_names:
            print("file name: ", file_name)
            if ".yml" in file_name:
                try:
                    diff = repo.git.show(hash, file_name)
                except:
                    continue
                if "test" in file_name:
                    type = "TEST_FILE"
                else:
                    type = "DEVELOPMENT_FILE"
                try:
                    write_to_file("TYPE:  ", type)
                    write_to_file("DIFF: ", diff)
                except Exception as e:
                    print(e)





def file_finder (hashes, repo_path):
    repo = Repo(repo_path)
    # hash_file_map = []
    # diff_counter_test = 0
    # diff_counter_develop = 0

    for idx in range(len(hashes) - 1):


        diff_index = repo.commit(hashes[idx]).diff(hashes[idx + 1], create_patch = True)
        write_to_file("HASH: ", hashes[idx])

        for diff_info in diff_index.iter_change_type('M'):
            if ".yml" in diff_info.a_blob.path:
                if "test" in diff_info.a_blob.path :
                    # print("T\n")
                    try:
                        write_to_file ("Type: ", "TEST Script")
                        write_to_file("DIFF: ", str(diff_info))
                    except Exception as e:
                        print(e)
                        

                    # diff_counter_test += 1
                    # print(diff_counter)
                    # exit()
                else:
                    # print("D\n")
                    # print(str(diff_info))
                    # diff_counter_develop += 1
                    try:
                        write_to_file ("Type: ", "Development Script")
                        write_to_file("DIFF: ", str(diff_info))
                    except Exception as e:
                        print(e)

            else:
                continue
    # print("Total found diffs in Test Scripts: ", diff_counter_test)
    # print("Total found diffs in Development Scripts: ", diff_counter_develop)
    # print(hashes)

    # for commit in list(repo.iter_commits()):
    #     # print(commit.hexsha)
    #     if commit.hexsha in hashes:
    #         files = commit.stats.files
    #         for file in files:
    #             if file.endswith('.yml'):
    #                 if "test" in file:
    #                     print("T\n")
    #                 else:
    #                     print("D\n")
                    
    #                 print(file)
        





def commit_finder(repo_path, file_path):
    repo = Repo(repo_path)
    commits = repo.iter_commits('--all', max_count=1000, paths=file_path)
    fixer_commits = []
    for commit in commits:
        commit_object = {}
        commit_message = clean_up(commit.message)
        # print("commiter name: ",commit.committer.name)
#         print ("commit message: ", commit.message)
        commit_object["bug_flag"] = 0
        if is_fixer_commit(keywords, commit_message):
            commit_object["bug_flag"] = 1
        commit_object["hash"] = commit.hexsha
        commit_object["message"] = commit_message
        fixer_commits.append(commit_object)

    return fixer_commits

        
def is_fixer_commit(keywords, commit_message):
    return any(keyword in commit_message for keyword in keywords)


def clean_up(string):
    return re.sub('[^A-Za-z0-9. ]+', ' ', string)


def commit_diff_finder():
    repo_names = fetch_project_names()
    print("repo_names: ", repo_names)
    
    for repo in repo_names:
        hashes = fetch_commit_hash(repo, 1)
        repo_path = find_repo_dir(repo)
        # write_to_file("Repo Name: ", repo)
        
        file_finder_v2(hashes, repo_path)




commit_diff_finder()
