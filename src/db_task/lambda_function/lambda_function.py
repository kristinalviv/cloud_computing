import sys
import logging
import pymysql
import json
import creds

# rds settings
rds_host  = creds.rds_host
user_name = creds.user_name
password = creds.password
db_name = creds.db_name


try:
    print('Here')
    conn = pymysql.connect(host=rds_host, user=user_name, db=db_name, passwd=password, connect_timeout=5)

    print("SUCCESS: Connection to RDS MySQL instance succeeded")
    
    def lambda_handler(event, context):
        record = json.loads(event["Records"][0]["body"])
        CustID = record["CustID"]
        Name = record["Name"]
        print(Name)
        print(CustID)
    
        sql_string = f"insert into Customer (CustID, Name) values({CustID}, '{Name}')"
    
        with conn.cursor() as cur:
            cur.execute("CREATE DATABASE if not exists test_db")
            cur.execute("USE test_db")
            cur.execute("create table if not exists Customer ( CustID  int NOT NULL, Name varchar(255) NOT NULL, PRIMARY KEY (CustID))")
            cur.execute(sql_string)
            conn.commit()
            cur.execute("select * from Customer")
            item_count = 0
            print("The following items have been added to the database:")
            for row in cur:
                item_count += 1
                print(row)
        conn.commit()
        conn.close()
except pymysql.MySQLError as e:
    print(e)
        
        
# adding this commented code here to view all previously inserted records into db
# try:
#     print('Here')
#     conn = pymysql.connect(host=rds_host, user=user_name, db=db_name, passwd=password, connect_timeout=5)

#     print("SUCCESS: Connection to RDS MySQL instance succeeded")
    
#     def lambda_handler(event, context):
#         with conn.cursor() as cur:
#             cur.execute("select * from Customer")
#             res =  cur.fetchall()
#             return res
#         conn.commit()
#         conn.close()
# except pymysql.MySQLError as e:
#     print(e)