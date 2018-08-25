import psycopg2
from config import config
import sys

input=sys.argv[1]
# input=sys[]
def institute_id():
    #""" update vendor name based on the vendor id """
    sql_sample= """SELECT * FROM sample WHERE id=1"""
    conn = None
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # print(cur)
        # execute the UPDATE  statement
        cur.execute(sql_sample, ())
        print('executed')
        for table in cur.fetchall():
            print(table)
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


# institute_id()

def publication_id():
    #""" update vendor name based on the vendor id """
    sql_sample= """SELECT * FROM sample"""
    conn = None
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # print(cur)
        # execute the UPDATE  statement
        cur.execute(sql_sample, ())
        # print('executed')
        for table in cur.fetchall():
            # print(table[3])
            if table[3]==24:
                print(table)
                # tab=table[3]
                # print(tab)

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


# publication_id()


def small_inst_checking():
    #""" update vendor name based on the vendor id """
    sql_sample= """SELECT * FROM sample"""
    conn = None
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # print(cur)
        # execute the UPDATE  statement
        cur.execute(sql_sample, ())
        # print('executed')
        for table in cur.fetchall():
            # print(table[3])
            if table[3]==24:
                # print(table)
                # tab=table[3]
                # print(tab)
                if table[4]==24:
                    # print("success",table)
                # else:
                    cur.execute("""DELETE FROM  sample WHERE sub_id=85""")
                    print("DELETED")
                    # print("so bad")
                    # conn = None
                    # try:
                    #     # read database configuration
                    #     params = config()
                    #     # connect to the PostgreSQL database
                    #     conn = psycopg2.connect(**params)
                    #     # create a new cursor
                    #     cur = conn.cursor()
                    #     # print(cur)
                    #     # execute the UPDATE  statement
                    #     cur.execute(sql_sample, ())
                    #     print('executed')
                    #     updated_rows = cur.rowcount
                    #     conn.commit()

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


small_inst_checking()


def show_tables():
    #""" update vendor name based on the vendor id """
    sql_sample= """SELECT * FROM sample ORDER BY id"""
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
            if table[4]==24:
                # print(table)
                if table[3]==10:
                    print(table)
                #     if table[3]==variable2:
                #         "update_2_var"
                #     else
                #         "auto_inctreament2"
                # else
                #     "auto_increament"
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


# show_tables()
