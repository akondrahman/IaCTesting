import requests, json, pymysql
db_conn = pymysql.connect("localhost","root","","test", charset='utf8' )
cursor = db_conn.cursor()

def fetch_repo_info(repo):
    payload = ''
    headers = {
            'Accept': 'application/vnd.github.v3+json',
            'User-Agent': 'talismanic',
            'Authorization': 'Basic dGFsaXNtYW5pYzoxMmMwNDgwMzQ0NGQzNGI5NjIwM2NkOGM4NzEwNDE5NDdkZmQzYmY1'
            }
    
    endpoint = "https://api.github.com/repos/" + repo[1]
    try:
        print("==========")
        print("Fetching repo meta data from Github Repos API\n===========")
        
        res_data = requests.request("GET", endpoint, headers=headers, data=payload)
        out = json.loads(res_data.text)
        try:
            if out["fork"] == True:
                is_fork = 1
            else:
                is_fork = 0
            repo_creation_date = out["created_at"]
        except:
            print(out)
            return
        print(is_fork)
            
#        
        update_query = "update github_repos_puppet set is_clone = %s, repo_creation_date = %s where id = %s"
        val = (is_fork, repo_creation_date ,repo[0])
        cursor.execute(update_query, val)
        db_conn.commit()
        
        return 1
        
        
    except Exception as e:
        print(e)
        return 0


def get_all_github_repo_id():
    
    try:
        cursor.execute('select * from github_repos_puppet where id>486 and no_of_developers>9 and is_clone is null')
        rows = cursor.fetchall()
    except:
        print(Exception)
        rows = []
        
    return rows


repos = get_all_github_repo_id()

for repo in repos:

    print (f'\n ***Repo ID is {repo[0]} ***\n\n')
    count = 0
    if repo[0]>0:
        fetch_repo_info(repo)