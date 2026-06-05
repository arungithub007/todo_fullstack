import pymysql

def get_conn():
    return pymysql.connect(host="localhost", user="root", password="root", database="todo")

def get_tasks():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT id, task FROM tasks")
    rows = cur.fetchall()
    conn.close()
    return [{"id": r[0], "task": r[1]} for r in rows]

def add_task(task):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("INSERT INTO tasks (task) VALUES (%s)", (task,))
    conn.commit()
    conn.close()

def update_task(task_id, new_task):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("UPDATE tasks SET task=%s WHERE id=%s", (new_task, task_id))
    conn.commit()
    conn.close()

def delete_task(task_id):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("DELETE FROM tasks WHERE id=%s", (task_id,))
    conn.commit()
    conn.close()
