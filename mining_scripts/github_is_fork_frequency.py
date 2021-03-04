# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 23:43:21 2021

@author: mehedi.md.hasan
"""

import requests, json, pymysql
from datetime import datetime
db_conn = pymysql.connect("localhost","root","","test", charset='utf8' )
cursor = db_conn.cursor()



def fetch_commit_stat(repo_name):
    payload = ''
    headers = {
            'Accept': 'application/vnd.github.cloak-preview',
            'User-Agent': 'talismanic',
            'Authorization': 'Basic dGFsaXNtYW5pYzoxMmMwNDgwMzQ0NGQzNGI5NjIwM2NkOGM4NzEwNDE5NDdkZmQzYmY1'
            }
    
    endpoint = "https://api.github.com/search/commits?q=repo:"+repo_name+"+committer-date:>2012-01-01&sort=committer-date&order=desc&per_page=1&page_number=1"
#    print(endpoint)
    try:
        print("==========")
        print("Fetching commit stats from Github Search API\n===========")
        
        res_data = requests.request("GET", endpoint, headers=headers, data=payload)
#        print(res_data)
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
    


def find_monthly_commit_frequency(repo):
    commit_stat = fetch_commit_stat(repo[1])
#    print(commit_stat)
    if commit_stat == None:
        print(commit_stat)
        return
    else:
        try:
            total_commit_count = commit_stat["total_count"]
            repo_creation_date = repo[7]
            last_commit_date = repo[8]       
            total_month = find_month_gap(repo_creation_date, last_commit_date)
            if total_month>0:
                monthly_commit_freq = total_commit_count/total_month
            else:
                monthly_commit_freq = 0
        
            update_query = "update github_repos_puppet set total_commits = %s,  monthly_commit_frequency = %s where id = %s"
            val = (total_commit_count,monthly_commit_freq, repo[0])
            cursor.execute(update_query, val)
            db_conn.commit()
        
    
      
            return monthly_commit_freq
        except Exception as e:
            print(e)
            return None


#def fork_frequency_details(repo):
#    repo_info = fetch_repo_info(repo)
    #print(repo_info)
#    if repo_info == None:
#        return 
#    else:
#    find_monthly_commit_frequency (repo)
    


def get_all_github_repo_id():
    
    try:
        cursor.execute('select * from github_repos_puppet where no_of_developers>9 and is_clone=0 and total_commits is null')
#        cursor.execute('select * from github_repos_puppet where id=18172')
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
        find_monthly_commit_frequency (repo)
    