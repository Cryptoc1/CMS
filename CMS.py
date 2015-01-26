import MySQLdb as mdb
import sys

version = "0.0.0b"
error_message = "There was an error when attempting to process your request. System returned: "

def get_all_posts():
    try:
        con = mdb.connect("localhost", "test", "test123", "CMS")

        cur = con.cursor()
        cur.execute("SELECT * FROM Posts")

        res = cur.fetchall()

        return res

    except mdb.Error, e:
        print error_message . e
        sys.exit(1)

    finally:
        if con:
            con.close()

def new_post():
    try:
        con = mdb.connect("localhost", "test", "test123", "CMS")

        cur = con.cursor()
        cur.execute("")

        ''' 
        if POST successful:
            print success message
        elif:
            print error message
        '''

    except mdb.Error, e:
        print error_message . e
        sys.exit(1)

    finally:
        if con:
            con.close()

def version():
    print version
