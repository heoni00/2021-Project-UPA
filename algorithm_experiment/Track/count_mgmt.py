from inventory_db import conn_mysqldb
import pandas as pd
import datetime
class Count():
    @staticmethod
    def get_count(model, location): # 특정 장소의 특정 차 수량 정수형 반환
        mysql_db = conn_mysqldb()
        db_cursor = mysql_db.cursor()
        sql = "SELECT * FROM model_count WHERE MODEL = '" + str(model) + "' AND LOCATION = '" + str(location) + "'"
        db_cursor.execute(sql)
        count = db_cursor.fetchone()[1]
        return count

    @staticmethod
    def get_all():
        mysql_db = conn_mysqldb()
        db_cursor = mysql_db.cursor()
        sql = "SELECT * FROM model_count"
        db_cursor.execute(sql)
        df = pd.DataFrame(db_cursor.fetchall())
        df.columns =['MODEL', 'COUNT', 'LOCATION']
        return df

    @staticmethod
    def get_location_count(location): # 특정 장소의 모든 차 수량 합 정수형 반환
        mysql_db = conn_mysqldb()
        db_cursor = mysql_db.cursor()
        sql = "SELECT * FROM model_count WHERE LOCATION = '" + str(location) + "'"
        db_cursor.execute(sql)
        infos = db_cursor.fetchall()
        count = 0
        for info in infos:
            count += info[1]
        return count

    @staticmethod
    def get_model_count(model):  # 모든 장소의 특정 차 수량 합 정수형 반환
        mysql_db = conn_mysqldb()
        db_cursor = mysql_db.cursor()
        sql = "SELECT * FROM model_count WHERE MODEL = '" + str(model) + "'"
        db_cursor.execute(sql)
        infos = db_cursor.fetchall()
        count = 0
        for info in infos:
            count += info[1]
        return count

    @staticmethod
    def plus_count(model, location, count):
        mysql_db = conn_mysqldb()
        db_cursor = mysql_db.cursor()
        sql = "UPDATE model_count SET COUNT = COUNT + "+ str(count) + " WHERE MODEL = '" + str(model) + "' AND LOCATION = '" + str(location) + "'"
        db_cursor.execute(sql)
        mysql_db.commit()
        return count

    @staticmethod
    def minus_count(model, location, count):
        mysql_db = conn_mysqldb()
        db_cursor = mysql_db.cursor()
        sql = "UPDATE model_count SET COUNT = COUNT - " + str(count) + " WHERE MODEL = '" + str(model) + "' AND LOCATION = '" + str(location) + "'"
        db_cursor.execute(sql)
        mysql_db.commit()
        return count

    @staticmethod
    def create(model, count, location):
        mysql_db = conn_mysqldb()
        db_cursor = mysql_db.cursor()
        sql = "INSERT INTO model_count (MODEL, COUNT, LOCATION) VALUES ('%s', '%s', '%s')" % (str(model), str(count), str(location))
        db_cursor.execute(sql)
        mysql_db.commit()
        return count

    # @staticmethod
    # def create_table():
    #     models = ['VSR', 'AVT', 'AVTH', 'i30', 'IOH', 'IOE', 'IOE5', 'G70',
    #               'G80', 'G90', 'VNU', 'KON', 'KOH', 'NKON', 'KOE', 'TUC', 'TUCH',
    #               'STF', 'STFH', 'PSD', 'GV70', 'GV80','PTR', 'G80E']
    #     mysql_db = conn_mysqldb()
    #     db_cursor = mysql_db.cursor()
    #     for model in models:
    #         sql = "INSERT INTO model_count (MODEL,COUNT,LOCATION) VALUES ('%s',0,'YARD');" % (model)
    #         db_cursor.execute(sql)
    #         mysql_db.commit()
    #         sql = "INSERT INTO model_count (MODEL,COUNT,LOCATION) VALUES ('%s',0,'6wharf');" % (model)
    #         db_cursor.execute(sql)
    #         mysql_db.commit()