import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn


def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def main():
    database = "./db_folder/pen-kl.db"

    sql_create_projects_table = """ CREATE TABLE IF NOT EXISTS flights (
                                        queryTime text NOT NULL,
                                        flightDate text NOT NULL,
                                        depTime text NOT NULL,
                                        arrTime text NOT NULL,
                                        price int NOT NULL,
                                        CONSTRAINT COMP_NAME PRIMARY KEY (queryTime, flightDate, depTime, arrTime)
                                    ); """

    sql_create_tasks_table = """CREATE TABLE IF NOT EXISTS flightTime (
                                    flightDate_date text NOT NULL,
                                    depTime text NOT NULL,
                                    arrTime text NOT NULL,
                                    price int NOT NULL,
                                    FOREIGN KEY (flightDate_date) REFERENCES dates (flightDate),
                                    CONSTRAINT COMP_NAME PRIMARY KEY (flightDate_date, depTime, arrTime)
                                );"""

    # create a database connection
    conn = create_connection(database)

    # create tables
    if conn is not None:
        # create projects table
        create_table(conn, sql_create_projects_table)

        # create tasks table
        #create_table(conn, sql_create_tasks_table)
    else:
        print("Error! cannot create the database connection.")


if __name__ == '__main__':
    main()
    
#check if tables are in by doing (sqlite3 ./pathtodb , .tables)