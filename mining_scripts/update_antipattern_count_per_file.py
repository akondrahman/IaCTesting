import re
import pymysql
import  re
db_conn = pymysql.connect(host='localhost',
                      user='root',
                      password='',
                      database='test',
                      charset='utf8')
cursor = db_conn.cursor()


# def clean_up(string):
#     return re.sub('[^A-Za-z0-9. ]+\"', ' ', string)

def fetch_data():
    try:
        cursor.execute('select * from commit_messages_16 where bugflag = 1 and bug_script_type > -1 ')
        # cursor.execute('select distinct project_name from iac_anti_patterns_v2 where repo_type=1  limit 5')
        # select_query = """select distinct project_name from commit_messages where bugflag = bugflag limit 1"""
        # cursor.execute(select_query, (bugflag) )
        rows = cursor.fetchall()
        final_result = [i for i in rows]
        # print("rows: " ,rows)
    except:
        print(Exception)
        final_result = []
        
    return final_result

def fetch_antipattern_count(project_name, file_name):
    try:
        select_query = 'select * from iac_anti_patterns_v2 where project_name = %s and file_name=%s '
        # cursor.execute('select distinct project_name from iac_anti_patterns_v2 where repo_type=1  limit 5')
        # select_query = """select distinct project_name from commit_messages where bugflag = bugflag limit 1"""
        cursor.execute(select_query, (project_name, file_name) )
        rows = cursor.fetchall()
        final_result = [i for i in rows]
        # print("rows: " ,rows)
    except:
        print(Exception)
        final_result = []
        
    return final_result


def update_antipattern_count(id, SAL, LOT, AR, ED, NEC):
    upd_query = 'update commit_messages_16 set SAL = %s, LOT = %s, AR = %s, ED = %s, NEC = %s where id =%s'
    val = (SAL, LOT, AR, ED, NEC, id)
    try:
        # print(ins_query)
        cursor.execute(upd_query, val)
        # print(upd_query)
        db_conn.commit()
        # print(f'Updated repo: {project} ')
    except Exception as e:

        print ("Exception while update: ", e)



def update_orchestration():
    all_data = fetch_data()
    
    for data in all_data:
	    anti_pattern = fetch_antipattern_count(data[1], data[3])
	    update_antipattern_count(data[0], data[5], data[6], data[7], data[8], data[9])


update_orchestration()