import glob, os, pymysql
db_conn = pymysql.connect("localhost","root","","test", charset='utf8' )
cursor = db_conn.cursor()



def count_yml_files(base_dir):
    yml_counter = 0
    
    for (dirpath, dirnames, filenames) in os.walk(base_dir):
        for file in filenames:
            if file.endswith(".yml") or file.endswith(".yaml"):
                yml_counter = yml_counter + 1
    
    print(f'yml file count:{yml_counter}')
    
    return  yml_counter
# count_test_files(r"C:\mined_repos\guardianproject-ops")

def get_all_repos():
   
    try:
        cursor.execute('select * from final_repos')
        rows = cursor.fetchall()
    except:
        print(Exception)
        rows = []
       
    return rows

def update_db (repo_id, total_yml_files):
    update_query = "update final_repos set total_yml_files = %s where id = %s"
    val = (total_yml_files, repo_id)
    cursor.execute(update_query, val)
    db_conn.commit()   




repos = get_all_repos()
base_dir = r"C:\mined_repos"
for repo in repos:

    repo_id = repo[0]
    top_dir = repo[1].split("/")[0]
    project_dir = repo[1].split("/")[1]
    full_dir = base_dir+"\\"+top_dir+"\\"+project_dir
    project_name = top_dir+"_"+project_dir
    print(f'full directory is {full_dir}')
    yml_files = count_yml_files(full_dir)
    print(f"yml files are {yml_files}")
    try:
        update_db(repo_id, yml_files)
        print(f'Update repo {repo_id} with total yml files {yml_files}')
    
    except Exception as e:
        print(e)
        continue
    
