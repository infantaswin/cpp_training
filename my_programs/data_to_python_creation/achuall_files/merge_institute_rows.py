#!/usr/bin/python

import sys
import psycopg2
import json
from slugify import slugify
from config import config


def update_institute(data, keep_id):
    """ update institute details from json file """

    name        =   data['name']
    federation  =   data['federation']
    acronym     =   data['acronym']
    city        =   data['city']
    state       =   data['state']
    country     =   data['country']
    slug        =   slugify(name)

    sql = """ UPDATE library_institute
              SET name = %s,
              federation = %s,
              acronym = %s,
              city = %s,
              state = %s,
              country = %s,
              slug= %s
              WHERE id = %s"""
    conn = None
    updated_rows = 0
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSycQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the UPDATE  statement
        cur.execute(sql, (name, federation, acronym, city, state, country, slug, keep_id))
        # get the number of updated rows
        updated_rows = cur.rowcount
        # Commit the changes to the database
        conn.commit()
        # Close communication with the PostgreSQL database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return updated_rows


def trasnfer(keep_id, transfer_id, sql):
    conn = None
    updated_rows = 0
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the UPDATE  statement
        cur.execute(sql, (keep_id, transfer_id, keep_id))
        # get the number of updated rows
        updated_rows = cur.rowcount
        # Commit the changes to the database
        conn.commit()
        # Close communication with the PostgreSQL database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return updated_rows


def clean_up(dele, sql):
    conn = None
    updated_rows = 0
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the UPDATE  statement
        cur.execute(sql, [dele])
        # get the number of updated rows
        updated_rows = cur.rowcount
        # Commit the changes to the database
        conn.commit()
        # Close communication with the PostgreSQL database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return updated_rows




if __name__ == '__main__':
    """ UPDATE library_author_institute SET institute_id='xxx' WHERE
        institute_id='yyy' AND author_id NOT IN (SELECT author_id from library_author_institute WHERE institute_id='xxx');
    """

    sql_auth = """ UPDATE library_author_institute
                SET institute_id = %s
                WHERE institute_id = %s
                AND author_id NOT IN
                (SELECT author_id from library_author_institute
                WHERE institute_id= %s)"""

    sql_pub = """ UPDATE library_publication_institutes
                SET institute_id = %s
                WHERE institute_id = %s
                AND publication_id NOT IN
                (SELECT publication_id from library_publication_institutes
                WHERE institute_id= %s)"""

    clean_pub  = """
                DELETE FROM library_publication_institutes
                WHERE institute_id = %s"""
    clean_auth = """
                DELETE FROM library_author_institute
                WHERE institute_id = %s"""

    clean_row = """ DELETE FROM library_institute WHERE id = %s"""



    data_file = sys.argv[1]
    with open(data_file) as json_file:
        data = json.load(json_file)
        print('Cleaning up ' + data['name'])

        ids          = data['id']
        keep         = ids[0]
        transfer_ids = ids[1:]

        for trans in transfer_ids:
            auth = trasnfer(keep, trans, sql_auth)
            pub = trasnfer(keep, trans, sql_pub)

        for dele in transfer_ids:
            clean_up(dele, clean_pub)
            clean_up(dele, clean_auth)
            clean_up(dele, clean_row)

        update_institute(data, keep)
