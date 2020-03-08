import sqlite3
from sqlite3 import Error
from queries import create_table_queries, drop_table_queries

def create_database(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    
    cur = conn.cursor()
    
    return cur, conn


def drop_tables(cur, conn):
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()
        

def create_tables(cur, conn):
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    """
    Driver main function.
    """
    cur, conn = create_database('GTA_Vehicles.db')
    
    drop_tables(cur, conn)
    print("Table drop success")

    create_tables(cur, conn)
    print("Table create success")

    conn.close()

    
if __name__ == "__main__":
    main()
      

