import requests, json, pymysql
from datetime import datetime
db_conn = pymysql.connect("localhost","root","","test", charset='utf8' )
cursor = db_conn.cursor()

def fetch_repo_info(repo):
    payload = ''
    headers = {
            'Accept': 'application/vnd.github.v3+json',
            'User-Agent': 'talismanic',
            'Authorization': 'Basic 8d7f429fa6db14647778a05a2503b861e56e6ba0'
            }
    
    endpoint = "https://api.github.com/repos/" + repo[1]
    try:
        print("==========")
        print("Fetching repo meta data from Github Repos API\n===========")
        
        res_data = requests.request("GET", endpoint, headers=headers, data=payload)
        out = json.loads(res_data.text)
        
        update_query = "update github_repos set is_clone = %s, repo_creation_date = %s where id = %s"
        val = (out["fork"],out["created_at"] ,repo[0])
        cursor.execute(update_query, val)
        db_conn.commit()
        
    
        return out
        
    except Exception as e:
        print(e)
        return None

def is_fork(repo_meta_data, repo):
    if repo_meta_data["fork"] == "True":
        return True
    else:
        return False


def fetch_commit_stat(repo_name):
    payload = ''
    headers = {
            'Accept': 'application/vnd.github.cloak-preview',
            'User-Agent': 'talismanic',
            'Authorization': 'Basic 8d7f429fa6db14647778a05a2503b861e56e6ba0'
            }
    
    endpoint = "https://api.github.com/search/commits?q=repo:"+repo_name+"+committer-date:>2012-01-01&sort=committer-date&order=desc&per_page=1&page_number=1"
    try:
        print("==========")
        print("Fetching commit stats from Github Search API\n===========")
        
        res_data = requests.request("GET", endpoint, headers=headers, data=payload)
        out = json.loads(res_data.text)
        
        return out
        
    except Exception as e:
        print(e)
        return None
        
        
def find_month_gap(start_date, end_date):
    d1 = start_date.split("T")[0]
    print(f'repo creation date: {d1}')
    d1 = datetime.strptime(d1, '%Y-%m-%d').date()
    d2 = end_date.split("T")[0]
    print(f'last commit date: {d2}')
    d2 = datetime.strptime(d2, '%Y-%m-%d').date()
    return (d2.year - d1.year) * 12 + (d2.month - d1.month)
    


def find_monthly_commit_frequency(repo, repo_creation_date):
    commit_stat = fetch_commit_stat(repo[1])
    if commit_stat == None:
        return
    else:
        try:
            total_commit_count = commit_stat["total_count"]
            last_commit_date = commit_stat["items"][0]["commit"]["committer"]["date"]       
            total_month = find_month_gap(repo_creation_date, last_commit_date)
            monthly_commit_freq = total_commit_count/total_month
        
            update_query = "update github_repos set total_commits = %s, last_commit_date = %s, monthly_commit_frequency = %s where id = %s"
            val = (total_commit_count,last_commit_date,monthly_commit_freq, repo[0])
            cursor.execute(update_query, val)
            db_conn.commit()
        
    
            print(f'last commit date : {last_commit_date}')
            return monthly_commit_freq
        except Exception as e:
            print(e)
            return None


def fork_frequency_details(repo):
    repo_info = fetch_repo_info(repo)
    #print(repo_info)
    if repo_info == None:
        return 
    else:
        is_forked = is_fork(repo_info, repo)
        repo_creation_date = repo_info["created_at"]
        print(f'Repo creation date is : {repo_creation_date}')
        commit_frequency = find_monthly_commit_frequency (repo, repo_creation_date)
    
        print(f'IS_FORKED: {is_forked} and commit frequency is {commit_frequency} per month')



def get_all_github_repo_id():
    
    try:
        cursor.execute('select * from github_repos')
        rows = cursor.fetchall()
    except:
        print(Exception)
        rows = []
        
    return rows

   
#print(fetch_commit_stat("redis/redis"))

#find_monthly_commit_frequency("redis/redis")
#print(find_month_gap("2015-07-25T10:53:05", "2020-11-13T21:16:40.000+08:00"))


repos = get_all_github_repo_id()

for repo in repos:

    print (f'\n ***Repo ID is {repo[0]} ***\n\n')
    count = 0
    if repo[0]>0:
        fork_frequency_details(repo)