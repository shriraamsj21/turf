import pymysql
from dotenv import load_dotenv
import os

load_dotenv()

connection = pymysql.connect(
    host=os.getenv('DB_HOST'),
    user=os.getenv('DB_USER'),
    password=os.getenv('DB_PASSWORD'),
    port=int(os.getenv('DB_PORT')),
)

cursor = connection.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS turf_db;")
connection.commit()
connection.close()
print("Database turf_db created successfully.")
