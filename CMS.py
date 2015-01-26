#!/usr/bin/env python
import MySQLdb as mdb
import sys

ver = "0.0.0b"
error_message = "There was an error when attempting to process your request. System returned: "

class CMS:
    def __init__(self, hostname, username, password, db):
        self.hostname = hostname
        self.username = username
        self.password = password
        self.db = db

    def set_hostname(self, hostname):
        self.hostname = hostname

    def get_hostname(self):
        return self.hostname

    def set_username(self, username):
        self.username = username

    def get_username(self):
        return self.username

    def set_pasword(self, password):
        self.password = password

    def get_password(self):
        return self.password

    def set_db(self, db):
        self.db = db

    def get_db(self):
        return self.db

    def get_all_posts(self):
        try:
            con = mdb.connect(self.hostname, self.username, self.password, self.db)

            cur = con.cursor()
            cur.execute("SELECT * FROM Posts")

            res = cur.fetchall()

            return res

        except mdb.Error, e:
            print error_message + e
            sys.exit(1)

        finally:
            if con:
                con.close()

    def get_post(self, pid, title, author):
        if pid:
            req = "SELECT * FROM Posts WHERE pid=" + pid
        elif title:
            req = "SELECT * FROM Posts WHERE title=" + title
        elif author:
            req = "SELECT * FROM Posts WHERE author=" + author

        try:
            con = mdb.connect(self.hostname,  self.username, self.password, self.db)
        
        except mdb.Error, e:
            print error_message + e

        finally:
            if con:
                con.close()
    def new_post():
        try:
            con = mdb.connect(self.hostname, self.username, self.password, self.db)

            cur = con.cursor()
            cur.execute("")

            ''' 
            if POST successful:
                print success message
            elif:
                print error message
            '''

        except mdb.Error, e:
            print error_message + e
            sys.exit(1)

        finally:
            if con:
                con.close()

    def version():
        print ver
