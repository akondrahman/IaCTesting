import gitlab
import pymysql, requests, json
from datetime import datetime
#set GIT_PYTHON_GIT_EXECUTABLE=C:\Program Files\Git\cmd\git.exe
db_conn = pymysql.connect("localhost","root","","test", charset='utf8' )
cursor = db_conn.cursor()

gl = gitlab.Gitlab('https://gitlab.com', private_token='ym_J9_F6GBXf4yF2ToQs')

def gitlab_search(per_page_item, page_number):
    search_str = 'puppet'
    search_scope = 'projects'
    search_results = gl.search(search_scope, search_str, page=page_number, per_page = per_page_item)
    # cur_page = search_results.current_page
    # print(f'current page: {search_results.current_page}')
    # print(f'Next page: {search_results.next_page}')
    # print(f'Length of output: {len(search_results)}')
    count = 0
    for search_result in search_results:
        count +=1
        # print(search_result)
        project_id = search_result['id']
        repo_name = search_result['path_with_namespace']
        repo_url = search_result['web_url']
        repo_creation_date = search_result['created_at']
        last_commit_date = search_result['last_activity_at']
        repo_lifetime_in_month = find_month_gap(repo_creation_date, last_commit_date)
        insert_query = "insert into gitlab_repos_puppet set id = %s, repo_name = %s, repo_url = %s, repo_creation_date = %s, last_commit_date = %s, repo_lifetime_in_month = %s"
        val = (project_id, repo_name, repo_url, repo_creation_date, last_commit_date, repo_lifetime_in_month)
        
        try:
            cursor.execute(insert_query, val)
            db_conn.commit()
        except Exception as e:
            print(e)
            continue



        print(f'====\nCount of repos in this iteration is: {count}====\n')
        # print(search_result.current_page())
    return count


def find_month_gap(start_date, end_date):
    d1 = start_date.split("T")[0]
    print(f'repo creation date: {d1}')
    d1 = datetime.strptime(d1, '%Y-%m-%d').date()
    d2 = end_date.split("T")[0]
    print(f'last commit date: {d2}')
    d2 = datetime.strptime(d2, '%Y-%m-%d').date()
    return (d2.year - d1.year) * 12 + (d2.month - d1.month)


def find_total_repos():
    repo_count = 0
    for i in range(500,1000):
            per_page = 20
            page_number = i + 1
            search_return = gitlab_search(per_page, page_number)
            repo_count = repo_count + search_return

            if search_return < per_page:
                print(f'Found total {repo_count} repositories')
                return repo_count
    

    return repo_count
    


find_total_repos()

# gitlab_search(1,1)
# get_project_members(22587785)