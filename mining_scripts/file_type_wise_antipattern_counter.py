import glob, os, pymysql
db_conn = pymysql.connect("localhost","root","","test", charset='utf8' )
cursor = db_conn.cursor()




def get_all_project_names():
   
    try:
        cursor.execute('select distinct project_name from iac_anti_patterns')
        rows = cursor.fetchall()
    except:
        print(Exception)
        rows = []
       
    return rows

def get_all_filenames(project_name):
    try:
        select_query ='select file_name, Skip_Ansible_Lint,Local_Only_Test,Assertion_Roulette,External_Dependency,No_ENV_CleanUp from iac_anti_patterns where project_name=%s'
        cursor.execute(select_query, (project_name,))
        rows = cursor.fetchall()
    except Exception as e:
        print(e)
        rows = []
       
    return rows


def update_db (base_dir):
    py_counter, yml_counter, total_test_files = count_test_files(base_dir)
    print(f'Updating test file count of repo {repo[0]} with values {py_counter}, {yml_counter}, {total_test_files} ')
    update_query = "update project_wise_file_count set python_test_files = %s, yml_test_files = %s, total_test_files = %s where id = %s"
    val = (py_counter, yml_counter, total_test_files, repo[0])
    cursor.execute(update_query, val)
    db_conn.commit()   


def create_bas_dir(project_name):
    base_dir = r"C:\mined_repos"
    l1 = project_name.split("_")[0]
    return base_dir+"\\"+l1


files= get_all_filenames('aepyornis_nyc-db')
print(files)
