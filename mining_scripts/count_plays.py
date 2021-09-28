import pymysql, yaml

db_conn = pymysql.connect(host='localhost',
                      user='root',
                      password='',
                      database='test',
                      charset='utf8')

cursor = db_conn.cursor()


def fetch_test_script_names():
    try:
        # cursor.execute('select distinct project_name from iac_anti_patterns_v2 where repo_type=1')
        # cursor.execute('select distinct project_name from iac_anti_patterns_v2 where repo_type=1  limit 5')
        select_query = """select distinct file_name from  commit_messages_23 where id > 0"""
        cursor.execute(select_query)
        rows = cursor.fetchall()
    except Exception as e:
        print(e)
        rows = []
        
    return rows

def get_playbook(file_path):

    with open(file_path, 'r') as f:
        # print(f'file path {file_path}')
        try:
            playbook = yaml.load(f)
        except Exception as e:
            
            print(e)
            return None
    
    return playbook


def find_plays_in_playbook(playbook):
    play_count = 0
    
    try:
        for role in playbook:
            # print(f'role name is {role}')

            try:
                try:
                    tasks = role['tasks']
                except:
                    tasks = role['post_task']
            
                for task in tasks:
                    # print(f'task name: {task}')
                    play_count += 1
            except:
                play_count += 1
                continue
    except Exception as e:
        print(e)
    return play_count

def insert_play_count(file_name, count):
    ins_query = 'insert into play_count (file_name, play_count) values (%s, %s)'
    val = (file_name, count)
    try:
        # print(ins_query)
        cursor.execute(ins_query, val)
        db_conn.commit()
        # print(f'Updated repo {project_name}')
    except Exception as e:
        print (e)

def counter():
    file_names = fetch_test_script_names()
    for file_name in file_names:
        file_path = file_name[0]
        # print(f'file name is {file_path}')
        playbook = get_playbook(file_path)
        play_count = find_plays_in_playbook(playbook)
        # print(f'file name {file_name[0]}, play count {play_count}')
        insert_play_count(file_path, play_count)



counter()
