import glob, os, pymysql
db_conn = pymysql.connect("localhost","root","","test", charset='utf8' )
cursor = db_conn.cursor()




def get_all_project_names():
   
    try:
        cursor.execute('select  * from project_wise_file_count limit 2')
        rows = cursor.fetchall()
    except:
        print(Exception)
        rows = []
       
    return rows

def get_all_project_meta(project_name):
    try:
        select_query ='select file_name, Skip_Ansible_Lint,Local_Only_Test,Assertion_Roulette,External_Dependency,No_ENV_CleanUp from iac_anti_patterns where project_name=%s'
        cursor.execute(select_query, (project_name,))
        rows = cursor.fetchall()
    except Exception as e:
        print(e)
        rows = []
       
    return rows


def update_db(project, py_SAL , py_LOT , py_AR , py_ED , py_NEC , yml_SAL , yml_LOT , yml_AR , yml_ED , yml_NEC):
    update_query = "update file_type_wise_antpatterns set py_SAL =%s py_LOT =%s py_AR =%s py_ED =%s py_NEC =%s yml_SAL =%s yml_LOT =%s yml_AR =%s yml_ED =%s yml_NEC =%s where project_name = %s"
    val = (py_SAL , py_LOT , py_AR , py_ED , py_NEC , yml_SAL , yml_LOT , yml_AR , yml_ED , yml_NEC, project )
    cursor.execute(update_query, val)
    db_conn.commit()   

def get_anti_pattern_count (project_name, file_name):
    try:
        select_query ='select * from iac_anti_patterns where project_name=%s and file_name=%s'
        cursor.execute(select_query, (project_name,file_name))
        rows = cursor.fetchall()
        print(rows)

    except Exception as e:
        print(e)
        return False
       
    return rows


projects = get_all_project_names()

for project in projects:    
    print(f'selected project name is : {project[1]}')
    project_metas = get_all_project_meta(project[1])
    print(f'No of files is in project {project[1]}:  {len(project_metas)}')
    py_SAL = py_LOT = py_AR = py_ED = py_NEC = yml_SAL = yml_LOT = yml_AR = yml_ED = yml_NEC =0
    
    for meta in project_metas:
        file_name = meta[0]
        print(f'file name is: {file_name}')
        print(get_anti_pattern_count (project[1], file_name))

        if file_name.endswith(".py"):
            
            anti_pattern_counts = get_anti_pattern_count (project[1], file_name)
            # print(f"Entered here {anti_pattern_counts(3)}")
            # print(f"Entered here {anti_pattern_counts[4]}")
            # print(f"Entered here {anti_pattern_counts[5]}")
            # print(f"Entered here {anti_pattern_counts[6]}")
            # print(f"Entered here {anti_pattern_counts[7]}")
            
            py_SAL = py_SAL + anti_pattern_counts[3]
            py_LOT = py_LOT + anti_pattern_counts[4]
            py_AR = py_AR + anti_pattern_counts[5]
            py_ED = py_ED + anti_pattern_counts[6]
            py_NEC = py_NEC + anti_pattern_counts[7]


            
        if file_name.endswith(".yml") or file_name.endswith(".yaml"):
            anti_pattern_counts = get_anti_pattern_count (project[1], file_name)
            print("Entered here")
            yml_SAL = yml_SAL + anti_pattern_counts[3]
            yml_LOT = yml_LOT + anti_pattern_counts[4]
            yml_AR = yml_AR + anti_pattern_counts[5]
            yml_ED = yml_ED + anti_pattern_counts[6]
            yml_NEC = yml_NEC + anti_pattern_counts[7]

            
        if file_name.endswith(".ini"):
            continue
    print(f'count of py_SAL , py_LOT , py_AR , py_ED , py_NEC , yml_SAL , yml_LOT , yml_AR , yml_ED , yml_NEC is {py_SAL}, {py_LOT}, {py_AR },{py_ED },{py_NEC}, {yml_SAL}, {yml_LOT}, {yml_AR}, {yml_ED}, {yml_NEC}')
    # update_db(project[1], py_SAL , py_LOT , py_AR , py_ED , py_NEC , yml_SAL , yml_LOT , yml_AR , yml_ED , yml_NEC)