import sqlite3

class Database():
    def __init__(self):
        self.con = sqlite3.connect('todolist.db')
        self.cur = self.con.cursor()

    def get_task(self):
        query = "SELECT * FROM Tasks"
        result = self.cur.execute(query)
        Tasks = result.fetchall()
        return Tasks
    
    def add_new_task(self , new_title , new_description , new_priority ,new_time):
        try:
            query = f"INSERT INTO Tasks(Title,Description,Priority,Time) VALUES('{new_title}','{new_description}','{new_priority}','{new_time}') "
            self.cur.execute(query)
            self.con.commit()
            return True
        except:
            return False

    def remove_task(self, title):
        try:
            query = f"DELETE FROM Tasks WHERE Title = '{title}'"
            self.cur.execute(query)
            self.con.commit()
            return True
        except:
            return False
    
    def task_done(self, title, status):
        try:
            query = f"UPDATE Tasks SET isDone = '{status}' WHERE Title = '{title}'"
            self.cur.execute(query)
            self.con.commit()
            return True
        except:
            return False