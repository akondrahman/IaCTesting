import requests, json, pymysql, re
from datetime import datetime
db_conn = pymysql.connect("localhost","root","","test", charset='utf8' )
cursor = db_conn.cursor()

def fetch_repo_info(repo):
    payload = ''
    headers = {
            'Accept': 'application/vnd.github.v3+json',
            'User-Agent': 'akondrahman',
            'Authorization': 'Basic YWtvbmRyYWhtYW46OGQ3ZjQyOWZhNmRiMTQ2NDc3NzhhMDVhMjUwM2I4NjFlNTZlNmJhMA=='
            }
    
    endpoint = "https://api.github.com/repos/" + repo[1]
    try:
        print("==========")
        print("Fetching repo meta data from Github Repos API\n===========")
        
        res_data = requests.request("GET", endpoint, headers=headers, data=payload)
        print(res_data.status_code)

        if res_data.status_code == 404:
            update_query = "update github_repos set does_repo_exist = %s where id = %s"
            val = (0 ,repo[0])
            cursor.execute(update_query, val)
            db_conn.commit()
            return None
        elif res_data.status_code == 200:
            out = json.loads(res_data.text)
        # print(f'\n====\n{out} ======\n=====\n=====')
        
            update_query = "update github_repos set is_clone = %s, repo_creation_date = %s where id = %s"
            val = (out["fork"],out["created_at"] ,repo[0])
            cursor.execute(update_query, val)
            db_conn.commit()
        
    
            return out
        else:
            return None
        
    except Exception as e:
        print(e)
        return None

def is_fork(repo_meta_data, repo):
    if repo_meta_data["fork"] == "True":
        return True
    else:
        return False


        
    
def fork_created_at_update(repo):
    repo_info = fetch_repo_info(repo)
    if repo_info != None:
        is_forked = is_fork(repo_info, repo)
        repo_creation_date = repo_info["created_at"]
        print(f'Repo creation date is : {repo_creation_date}')
        print(f'IS_FORKED: {is_forked}')



def get_all_github_repo_id():
    
    try:
        cursor.execute('select * from github_repos where is_clone is not null and id > 1040')
        rows = cursor.fetchall()
    except:
        print(Exception)
        rows = []
        
    return rows


   
#print(fetch_commit_stat("redis/redis"))

#find_monthly_commit_frequency("redis/redis")
#print(find_month_gap("2015-07-25T10:53:05", "2020-11-13T21:16:40.000+08:00"))

def find_total_commits_n_last_commit_date(u,r, id):
    payload = ''
    headers = {
            'Accept': 'application/vnd.github.v3+json',
            'User-Agent': 'akondrahman',
            'Authorization': 'Basic YWtvbmRyYWhtYW46OGQ3ZjQyOWZhNmRiMTQ2NDc3NzhhMDVhMjUwM2I4NjFlNTZlNmJhMA=='
            }
    
    endpoint = "https://api.github.com/repos/" + repo[1] +'/commits?per_page=1'
    try:
        print("==========")
        print("Fetching commit meta data from Github Repos API\n===========")
        
        res_data = requests.request("GET", endpoint, headers=headers, data=payload)
        link_headers = res_data.headers["Link"]
        last_page_details = link_headers.split(',')[1]
        last_page_url = last_page_details.split(';')[0]
        last_page_no = last_page_url.split('=')[2]
        total_commits = last_page_no.strip('>')
        
        #last commit date
        out = json.loads(res_data.text)
        last_commit_date = out[0]["commit"]["committer"]["date"]
        print(f'====\nLast Commit date of repo no {repo[0]} is :{last_commit_date}\n====')
        

        # print(last_page_details)
        # print(last_page_url)
        # print(last_page_no)
        print(f'total commits: {total_commits}')
        update_query = "update github_repos set total_commits = %s, last_commit_date = %s where id = %s"
        val = (total_commits, last_commit_date ,id)

        cursor.execute(update_query, val)
        db_conn.commit()
    except Exception as e:
        print("Entered in Exception")
        print(e)
        return None




repos = get_all_github_repo_id()

print (f'Length of select is {len(repos)}')

for repo in repos:
    print(f'======\nRepo Id is :{repo[0]}')
    
    # fork_created_at_update(repo)
    repo_name = repo[1]
    u,r = repo_name.split("/")
    find_total_commits_n_last_commit_date(u,r, repo[0])