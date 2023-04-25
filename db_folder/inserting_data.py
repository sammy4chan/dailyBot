import sqlite3
from sqlite3 import Error
from datetime import datetime


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn


def create_date(conn, dates):
    """
    Create a new project into the projects table
    :param conn:
    :param project:
    :return: project id
    """
    sql = ''' INSERT INTO dates(queryTime, flightDate)
              VALUES(?,?) '''
    cur = conn.cursor()
    cur.execute(sql, dates)
    conn.commit()
    return cur.lastrowid


def create_entry(conn, task):
    """
    Create a new task
    :param conn:
    :param task:
    :return:
    """

    sql = ''' INSERT INTO flights(queryTime, flightDate, depTime, arrTime, price)
              VALUES(?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, task)
    conn.commit()
    return cur.lastrowid


def main():
    database = "./db_folder/flights.db"

    # create a database connection
    conn = create_connection(database)
    with conn:
        # create a new flightQuery entry
        queryDate:str = datetime.now().strftime("%d/%m/%Y")
        flightDate = "21/6/2023" #sample
        dates = (queryDate, flightDate)
        create_date(conn, dates)

        # test entry 1
        entry = ("24/6/2023", "10:05", "11:11", 69)

        # create tasks
        create_entry(conn, entry)


if __name__ == '__main__':
    main()
    
    #to check:
    #sqlite3 [path to db]
    #.header on
    #.mode column
    #SELECT * FROM tasks; 
    #or SELECT * FROM projects;