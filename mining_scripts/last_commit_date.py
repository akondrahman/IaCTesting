import requests, json, pymysql, re
from datetime import datetime
db_conn = pymysql.connect("localhost","root","","test", charset='utf8' )
cursor = db_conn.cursor()


def get_all_github_repo_id():
    
    try:
        cursor.execute('select * from github_repos')
        rows = cursor.fetchall()
    except:
        print(Exception)
        rows = []
        
    return rows




def find_last_commit_date(repo):
       

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
        out = json.loads(res_data.text)
        last_commit_date = out[0]["commit"]["committer"]["date"]
        print(f'====\nLast Commit date of repo no {repo[0]} is :{last_commit_date}\n====')
        update_query = "update github_repos set last_commit_date = %s where id = %s"
        val = (last_commit_date ,repo[0])
        cursor.execute(update_query, val)
        db_conn.commit()

        return last_commit_date
    
    except Exception as e:
        print(e)
        return None

	
repos = get_all_github_repo_id()
print(f'Total no of repos are: {len(repos)}')
for repo in repos:
    print(f'Repo id is: {repo[0]}')
    find_last_commit_date(repo)