import sqlite3

class Database():
    def __init__(self):
        self.con = sqlite3.connect('Alarms.db')
        self.cur = self.con.cursor()

    def get_alarms(self):
        query = "SELECT * FROM alarms"
        result = self.cur.execute(query)
        Alarms = result.fetchall()
        return Alarms
    
    def add_new_alarm(self ,new_time):
        try:
            query = f"INSERT INTO alarms(Time) VALUES('{new_time}') "
            self.cur.execute(query)
            self.con.commit()
            return True
        except:
            return False

    def remove_alarm(self, time):
        try:
            query = f"DELETE FROM alarms WHERE Time = '{time}'"
            self.cur.execute(query)
            self.con.commit()
            return True
        except:
            return False
        
    def edit_alarm(self,id, time):
        try:
            query = f"UPDATE alarms SET Time='{time}' WHERE ID='{id}'"
            self.cur.execute(query)
            self.con.commit()
            return True
        except:
            return False
