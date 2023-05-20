import sys
import logging
import pymysql
import json
import creds

# rds settings
rds_host  = creds.rds_host
new_rds_host  = creds.new_rds_host
user_name = creds.user_name
password = creds.password
db_name = creds.db_name

# # run before backup - data edition

# try:
#     print('Here')
#     conn = pymysql.connect(host=rds_host, user=user_name, db=db_name, passwd=password, connect_timeout=5)

#     print("SUCCESS: Connection to RDS MySQL instance succeeded")
    
#     def lambda_handler(event, context):
#         with conn.cursor() as cur:
#             cur.execute("UPDATE Customer SET Name = 'Violetta' WHERE CustID=1")
#             cur.execute("UPDATE Customer SET Name = 'George' WHERE CustID=2")
#             conn.commit()
#             cur.execute("select * from Customer")
#             res =  cur.fetchall()
#             return res
#         conn.commit()
#         conn.close()
# except pymysql.MySQLError as e:
#     print(e)


# run after backup to view restored data
# we can see in output "new" word
#print("SUCCESS: Connection to new RDS MySQL instance succeeded")

try:
    print('Here')
    conn = pymysql.connect(host=new_rds_host, user=user_name, db=db_name, passwd=password, connect_timeout=5)

    print("SUCCESS: Connection to new RDS MySQL instance succeeded")
    
    def lambda_handler(event, context):
        with conn.cursor() as cur:
            cur.execute("select * from Customer")
            res =  cur.fetchall()
            return res
        conn.commit()
        conn.close()
except pymysql.MySQLError as e:
    print(e)