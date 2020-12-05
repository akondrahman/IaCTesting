import requests, json, pymysql, re
from datetime import datetime
db_conn = pymysql.connect("localhost","root","","test", charset='utf8' )
cursor = db_conn.cursor()


def find_month_gap(start_date, end_date):
    d1 = start_date.split("T")[0]
    print(f'repo creation date: {d1}')
    d1 = datetime.strptime(d1, '%Y-%m-%d').date()
    d2 = end_date.split("T")[0]
    print(f'last commit date: {d2}')
    d2 = datetime.strptime(d2, '%Y-%m-%d').date()
    return (d2.year - d1.year) * 12 + (d2.month - d1.month)
    


def find_monthly_commit_frequency(repo):
    try:
        dev_months = int(find_month_gap(repo[1],repo[2]))
        print(f'Total Dev Month is: {dev_months}')
        print(f'Total commits: {repo[3]}')
        if dev_months>0:
            monthly_commit_frequency = int(repo[3]/dev_months)
        else:
            monthly_commit_frequency = int(repo[3])
        print(f'Monthly commit frequency is {monthly_commit_frequency}\n====')
        update_query = "update github_repos set monthly_commit_frequency = %s, repo_lifetime_in_month = %s where id = %s"
        # print(update_query)
        val = (monthly_commit_frequency, dev_months , repo[0])
        cursor.execute(update_query, val)
        db_conn.commit()

        print(db_conn.commit())


    except Exception as e:
        print("Entered Exception Block")
        print(e)
        return None


def get_all_github_repo_id():
    
    try:
        cursor.execute('select id, repo_creation_date, last_commit_date, total_commits from github_repos where repo_creation_date is not null and last_commit_date is not null')
        rows = cursor.fetchall()
    except:
        print(Exception)
        rows = []
        
    return rows
	
repos = get_all_github_repo_id()
print(f'Total no of repos are: {len(repos)}')
for repo in repos:
    print(f'Repo id is: {repo[0]}')
    find_monthly_commit_frequency(repo)