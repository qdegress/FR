import mysql.connector
import pymysql
import sqlalchemy
from datetime import datetime
import pandas as pd
import numpy as np
# from main import empl_id

engine = sqlalchemy.create_engine('mysql+pymysql://sanjayds:123456789@192.168.5.179:3306/attendace_database',
                                  convert_unicode=True)
mydb = mysql.connector.connect(
    host="192.168.5.179",
    user="sanjayds",
    password="123456789",
    database="attendace_database"
)



def markAttendance(empl_id, employee_name):
    now = datetime.now().strftime("%Y %m %d %H:%M:%S")
    #    d = datetime.now().strftime("%Y-%m-%d")
    d1 = datetime.now().strftime("%d-%m-%Y")
    t = datetime.now().strftime("%H:%M")
    q1 = f"""SELECT * FROM attendace_database.attendance_in;"""
    df = pd.read_sql(q1, engine)
    try:
        df2 = pd.DataFrame(
            {'Employee ID': empl_id, 'Employee Name': employee_name, 'TIME': [t], 'DATE': [d1], 'In/Out': "IN"})
        df = df.append(df2, ignore_index=True)
        df.drop_duplicates(subset=["Employee Name", "TIME"], inplace=True)
        df.to_sql('attendance_in', con=engine, if_exists='replace', index=False)

    except Exception as e:
        print(e)
        pass