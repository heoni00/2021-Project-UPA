from inventory_db import conn_mysqldb
import pandas as pd
from datetime import datetime

class History():

    @staticmethod
    def find_all():
        mysql_db = conn_mysqldb()
        db_cursor = mysql_db.cursor()
        sql = "SELECT * FROM moving_history"
        # print (sql)
        db_cursor.execute(sql)
        df = pd.DataFrame(db_cursor.fetchall())
        df.columns =['MOVING_TIME', 'MODEL', 'M_FROM', 'M_TO', 'COUNT']
        return df

    @staticmethod
    def create(model, source, destination, count, moving_time=datetime.now().strftime('%Y-%m-%d %H:%M:%S')):
        mysql_db = conn_mysqldb()
        db_cursor = mysql_db.cursor()
        sql = "INSERT INTO moving_history (MOVING_TIME, MODEL, M_FROM, M_TO, COUNT) VALUES ('%s', '%s', '%s', '%s', '%s')" % (
        str(moving_time), str(model), str(source), str(destination), str(count))
        db_cursor.execute(sql)
        mysql_db.commit()

    @staticmethod
    def find_log(start_date, end_date):
        mysql_db = conn_mysqldb()
        db_cursor = mysql_db.cursor()
        sql = "SELECT * FROM moving_history WHERE MOVING_TIME >= '%s' AND MOVING_TIME <= '%s 23:59:59'" % (
        start_date, end_date)
        # print (sql)
        db_cursor.execute(sql)
        logs = db_cursor.fetchall()
        if len(logs) == 0:
            return 'None'
        else:
            logs_df = pd.DataFrame(logs, columns=['MOVING_TIME', 'MODEL', 'M_FROM', 'M_TO', 'COUNT'])
        return History.merge_df(logs_df)

    @staticmethod
    def find_model_log(model):
        mysql_db = conn_mysqldb()
        db_cursor = mysql_db.cursor()
        sql = "SELECT * FROM moving_history WHERE MODEL = '%s'" % (str(model))
        # print (sql)
        db_cursor.execute(sql)
        logs = db_cursor.fetchall()
        if len(logs) == 0:
            return 'None'
        else:
            logs_df = pd.DataFrame(logs, columns=['MOVING_TIME', 'MODEL', 'M_FROM', 'M_TO', 'COUNT'])
        return History.merge_df(logs_df)

    @staticmethod
    def merge_df(df):
        df['MOVING_TIME'] = df['MOVING_TIME'].dt.date
        result = pd.DataFrame(df.loc[0]).T
        for i in range(1,len(df)):
            tmp = df.loc[i]
            valid = 0
            for j in range(0,len(result)):
                if (tmp['MOVING_TIME'] == result.loc[j]['MOVING_TIME']) & (tmp['MODEL'] == result.loc[j]['MODEL']) & (tmp['M_FROM'] == result.loc[j]['M_FROM']) & (tmp['M_TO'] == result.loc[j]['M_TO']):
                    result.loc[j]['COUNT'] += tmp['COUNT']
                    break
                else:
                    valid += 1
            if valid == len(result):
                result.loc[len(result)] = tmp
        result = result.sort_values(by='MOVING_TIME', ascending=False)
        return result
# History.create('G80', 'Factory', 'Yard', 7)
# print(History.find_all()[0][0])
# print(type(History.find_all()[0][0]))
