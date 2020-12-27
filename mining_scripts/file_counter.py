import glob, os, pymysql
db_conn = pymysql.connect("localhost","root","","test", charset='utf8' )
cursor = db_conn.cursor()



def count_test_files(base_dir):
    yml_counter = 0

    for (dirpath, dirnames, filenames) in os.walk(base_dir):
            for dirname in dirnames:
                if dirname == "tests":
                    test_path = os.path.join(dirpath, dirname)
                    print(f'test path is: {test_path}')
                    for (dirpath2, dirnames2, filenames2) in os.walk(test_path):
                        for file in filenames2:
                            if file.endswith(".yml") or file.endswith(".yaml"):
                                yml_counter = yml_counter + 1
    
    print(f'yml file count:{yml_counter}')
    
    return  yml_counter

def get_all_repos():
   
    try:
        cursor.execute('select * from final_repos')
        rows = cursor.fetchall()
    except:
        print(Exception)
        rows = []
       
    return rows

def update_db (repo_id, total_test_files):
    update_query = "update final_repos set total_test_files = %s where id = %s"
    val = (total_test_files, repo_id)
    cursor.execute(update_query, val)
    db_conn.commit()   


def create_bas_dir(project_name):
    base_dir = r"C:\mined_repos"
    l1 = project_name.split("_")[0]
    return base_dir+"\\"+l1


repos = get_all_repos()
r_dir = r"C:\mined_repos"
for repo in repos:
    repo_id = repo[0]
    top_dir = repo[1].split("/")[0]
    project_dir = repo[1].split("/")[1]
    base_dir = r_dir+"\\"+top_dir+"\\"+project_dir
    test_file_count = count_test_files(base_dir)

    try:
        update_db(repo_id, test_file_count)
        print(f'Updated repo {repo_id } with total test files as {test_file_count}')

    except Exception as e:
        print(e)
        continue
        


