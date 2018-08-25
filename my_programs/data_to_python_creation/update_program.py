import psycopg2
from config import config


def update_vendor(name, id):
    #""" update vendor name based on the vendor id """
    sql_sample= """ UPDATE sample
                SET name = %s
                WHERE id = %s"""
    conn = None
    updated_rows = 0
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # print(cur)
        # execute the UPDATE  statement
        cur.execute(sql_sample, (name, id))
        print('executed')
        # get the number of updated rows
        updated_rows = cur.rowcount
        # print(updated_rows)
        # Commit the changes to the database
        conn.commit()
        # Close communication with the PostgreSQL database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


# update_vendor(aswin, 1)

def show_tables():
    #""" update vendor name based on the vendor id """
    sql_sample= """SELECT * from library_publication_institutes where institute_id = 899"""
    conn = None
    updated_rows = 0
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # curu = conn.cursor()
        # print(cur)
        # execute the UPDATE  statement
        cur.execute(sql_sample)
        print('executed')
        for table in cur.fetchall():
            print(table)
            # tab = table.split(',')
            # ta = tab[1]
            # print(ta)
        # curu.execute("""SELECT * FROM sample WHERE id=2 AND sub_id=34""")
        # for tables in curu.fetchall():
            # print(tables)
        # get the number of updated rows
        updated_rows = cur.rowcount
        # print(updated_rows)
        # Commit the changes to the database
        conn.commit()
        print()
        # Close communication with the PostgreSQL database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


show_tables()
