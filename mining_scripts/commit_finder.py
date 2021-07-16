from git import Repo, RemoteProgress
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


keywords = [" error ", " bug", " fix", " issue", " mistake", " incorrect", " fault", " defect" , " flaw", " exception" ]


# repo_path = r'C:\Personal\Research\mollie-api-php'
# file_path = r'C:\Personal\Research\mollie-api-php\src\Resources\MethodCollection.php'
# repo = Repo(repo_path)
repo_type = 1
not_found_repo = 0
not_found_file = 0


def fetch_project_names():
    try:
        # cursor.execute('select distinct project_name from iac_anti_patterns_v2 where repo_type=1')
        # cursor.execute('select distinct project_name from iac_anti_patterns_v2 where repo_type=1  limit 5')
        select_query = """select distinct project_name from iac_anti_patterns_v2 where repo_type= %s"""
        cursor.execute(select_query, (repo_type) )
        rows = cursor.fetchall()
    except:
        print(Exception)
        rows = []
        
    return rows

def fetch_test_files(project):
    try:
        select_query = """select file_name from iac_anti_patterns_v2 where project_name=%s"""
        cursor.execute(select_query, (project,))
        rows = cursor.fetchall()
    except:
        print(Exception)
        rows = []
        
    return rows


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


def download_github_repo(repo_name):

    ext_dir = r'C:\mined_repos'
    
    base_repo = repo_name.split("/")[0]

    full_dir = ext_dir+"\\"+base_repo
    if os.path.exists(full_dir):
        return os.path.join(full_dir, repo_name.split("/")[1])
    else :
        os.makedirs(full_dir)
    
    print(full_dir)
    # return full_dir
    
    
    repo_url = "https://github.com/"+repo_name
    # repo_url = "https://gitlab.com/"+repo_name
    try:
        print(f"starting to download repository {repo_name}")
        print("=================")
        git.Git(full_dir).clone(repo_url)
        print("Download completed")
        print("=================")    
        return full_dir+"//"+repo_name.split("/")[1]
       
    except Exception as e:
        print(e)
        return full_dir+"//"+repo_name.split("/")[1]




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


def commit_message_miner():
    projects = fetch_project_names()
    

    for project in projects:
        print("Project Name: ", project[0])
        repo_path = download_github_repo(project[0])
        if os.path.exists(repo_path):
            # print(repo_path)
            test_files = fetch_test_files(project[0])
            # print(test_files)

            for test_file in test_files:
                # print(test_file)
                if os.path.exists(test_file[0]):
                    # print(test_file)
                    fixer_commits = commit_finder(repo_path, test_file)
                    for commit in fixer_commits:
                        insert_commit_messages(project[0], repo_path, test_file, commit['hash'], commit['message'], commit['bug_flag'])
                else:
                    # not_found_file = not_found_file + 1
                    print("test file", test_file, "not found")
                    continue
        else:
            # not_found_repo = not_found_repo + 1
            print("Repository", repo_path, "not found")
            continue         

                




commit_message_miner()
# print("Repos not found", not_found_repo)
# print("files not found", not_found_file)
# print(is_fixer_commit(keywords, 'Merge pull request #1516 from JunqiZhang0/fix-creds-path-recognition\n\nMerged by Jenkins'))