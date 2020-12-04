import glob, os, pymysql
db_conn = pymysql.connect("localhost","root","","test", charset='utf8' )
cursor = db_conn.cursor()



def count_test_files(base_dir):
    py_counter = 0
    yml_counter = 0
    total_test_files = 0

    for (dirpath, dirnames, filenames) in os.walk(base_dir):
            for dirname in dirnames:
                if dirname == "tests":
                    test_path = os.path.join(dirpath, dirname)
                    print(f'test path is: {test_path}')
                    for (dirpath2, dirnames2, filenames2) in os.walk(test_path):
                        for file in filenames2:
                            if file.endswith(".py"):
                                py_counter = py_counter +1
                            if file.endswith(".yml") or file.endswith(".yaml"):
                                yml_counter = yml_counter + 1
    print(f'python file count: {py_counter}')
    
    print(f'yml file count:{yml_counter}')
    total_test_files = py_counter + yml_counter
    print(f'total test file count: {total_test_files}')
    
    # for (dirpath, dirnames, filenames) in os.walk(base_dir):
    #     for dirname in dirnames:
    #         if dirname == "tests":
    #             test_path = os.path.join(dirpath, dirname)
    #             print(f'test path is: {test_path}')
    #             for (testdirpath, testdirnames, testfilenames) in os.walk(test_path):
    #                 for testfile in testfilenames:
    #                     if file.endswith(".py"):
    #                         py_counter = py_counter +1
    #                     if file.endswith(".yml") or file.endswith(".yaml"):
    #                         yml_counter = yml_counter + 1

    return py_counter, yml_counter, total_test_files
# count_test_files(r"C:\mined_repos\guardianproject-ops")

def get_all_repos():
   
    try:
        cursor.execute('select id, project_name from project_wise_antipatterns')
        rows = cursor.fetchall()
    except:
        print(Exception)
        rows = []
       
    return rows

def update_db (base_dir):
    py_counter, yml_counter, total_test_files = count_test_files(base_dir)
    print(f'Updating test file count of repo {repo[0]} with values {py_counter}, {yml_counter}, {total_test_files} ')
    update_query = "update project_wise_antipatterns set python_test_files = %s, yml_test_files = %s, total_test_files = %s where id = %s"
    val = (py_counter, yml_counter, total_test_files, repo[0])
    cursor.execute(update_query, val)
    db_conn.commit()   


def create_bas_dir(project_name):
    base_dir = r"C:\mined_repos"
    l1 = project_name.split("_")[0]
    return base_dir+"\\"+l1


repos = get_all_repos()

for repo in repos:
    base_dir = create_bas_dir(repo[1])
    
    for filename in os.listdir(base_dir):
        if filename.endswith(".git"):
            print(f'Base Directory is : {base_dir}')
            update_db(base_dir)
        else:
            ll = repo[1].split("_")
            if len(ll) == 2:
                l2_base_dir = base_dir + "\\" + ll[1]
                print(f'Base Directory is : {l2_base_dir}')
                update_db(l2_base_dir)
            else:
                ll2 = ll[1: len(ll)]
                l3 = "_"
                l3 = l3.join(ll2)    
                print(l3)
                l3_base_dir = base_dir + "\\"+l3
                print(f'Base Directory is : {l3_base_dir}')
                update_db(l3_base_dir)

            

