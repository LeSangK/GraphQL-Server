import time
import mysql.connector
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "mysql+mysqlconnector://root:190727@db:3306/my_database_test"


def wait_for_connection():
    max_retries = 10
    retry_interval = 5
    retries = 0
    while retries < max_retries:
        try:
            config = {
                "user": "root",
                "password": "190727",
                "host": "db",
                "port": "3306",
                "database": "my_database_test",
            }
            cnx = mysql.connector.connect(**config)
            cnx.close()
            return True
        except mysql.connector.Error as e:
            print(f"Error: {e}. Retrying in {retry_interval} seconds...")
            time.sleep(retry_interval)
            retries += 1
    return False


if wait_for_connection():
    engine = create_engine(DATABASE_URL)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    Base = declarative_base()
else:
    print("Could not establish a connection to the database after multiple retries.")
    exit(1)
