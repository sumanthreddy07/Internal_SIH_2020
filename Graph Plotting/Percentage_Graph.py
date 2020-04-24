import cv2
import mysql.connector
from mysql.connector import Error
import matplotlib.pyplot as plt

per_y = [0] * 24
per_g = [0] * 24
k = [0]*24
kt = -1

connection = mysql.connector.connect(host='localhost',
                                            database='SIH',
                                            user='SIH_User',
                                            password='Octanef2@')


db_Info = connection.get_server_info()
print("Connected to MySQL Server version ", db_Info)
cursor = connection.cursor()

query = "select * from green;"

cursor.execute(query)
record = cursor.fetchall()
                
for row in record:
    kt = kt+1
    per_g[kt] = row[1]
    per_y[kt] = row[2]
    k[kt] = kt                 
    

plt.plot(k, per_g)
plt.xlabel('No of Months')
plt.ylabel('Percentage area')

plt.title('Green Area Graph') 
plt.show()

cursor.close()
connection.close()

                




        
        
        


