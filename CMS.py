#!/usr/bin/env python
import MySQLdb as mdb
import sys

ver = "0.0.0b"
error_message = "There was an error when attempting to process your request. System returned:\n"

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

    def get_entry_count(self):
        try:
            con = mdb.connect(self.hostname, self.username, self.password, self.db)

            cur = con.cursor()
            cur.execute("SELECT COUNT(*) FROM Posts;")

            res = cur.fetchone()

            return res[0]

        except mdb.Error, e:
            print error_message + str(e)
            sys.exit(1)
        finally:
            if con:
                con.close()

    def get_all_posts(self):
        try:
            con = mdb.connect(self.hostname, self.username, self.password, self.db)

            cur = con.cursor()
            cur.execute("SELECT * FROM Posts;")

            res = cur.fetchall()
            posts =[]
            for i in res:
                p = {}
                p["pid"] = i[0]
                p["title"] = i[1]
                p["author"] = i[2]
                p["content"] = i[3]
                posts.append(p)

            return posts

        except mdb.Error, e:
            print error_message + str(e)
            sys.exit(1)
        finally:
            if con:
                con.close()
    
    def get_post_by_id(self, pid):
        if pid:
            req = "SELECT * FROM Posts WHERE pid=\"" + str(pid) + "\";"
            try:
                con = mdb.connect(self.hostname,  self.username, self.password, self.db)
                
                cur = con.cursor()
                cur.execute(req)
                res = cur.fetchone()

                if res == None:
                    print error_message + "No results found, reponse from server: "
                else:
                    post = {}
                    post["pid"] = res[0]
                    post["title"] = res[1]
                    post["author"] = res[2]
                    post["content"] = res[3]

                return post

            except mdb.Error, e:
                print error_message + str(e)
                sys.exit(1)
            finally:
                if con:
                    con.close()
        else:
            print error_message + "No Post ID (pid) specified."
            sys.exit(1)

    def get_posts_by_title(self, title):
        if title:
            req = "SELECT * FROM Posts WHERE title=\"" + title + "\";"
            try:
                con = medb.connect(self.hostname, self.username, self.password, self.db)

                cur = con.cursor()
                cur.execute(req)
                res = cur.fetchone()

            except mdb.Error, e:
                print error_message + str(e)
                sys.exit(1)
            finally:
                if con:
                    con.close()
        else:
            print error_message + "No Post Title (title) specified."
            sys.exit(1)

    def get_posts_by_author(self, author):
        if author:
            req = "SELECT * FROM Posts WHERE author=\"" + author + "\";"
            try:
                con = mdb.connect(self.hostname, self.username, self.password, self.db)

                cur = con.cursor()
                cur.execute(req)

                res = cur.fetchone()

                return res

            except mdb.Error, e:
                print error_message + str(e)
                sys.exit(1)
            finally:
                if con:
                    con.close()
        else:
            print error_message + "No Post Author (author) specified."
            sys.exit(1)

    def new_post(title, author, content):
        if title and author and content:
            req = "INSERT INTO Posts (title, author, content) VALUES ("  + title + ", " + author + ", " + content + ");"
            try:
                con = mdb.connect(self.hostname, self.username, self.password, self.db)

                cur = con.cursor()
                cur.execute(req)

                ''' 
                if POST successful:
                    print success message
                elif:
                    print error message
                '''

            except mdb.Error, e:
                print error_message + str(e)
                sys.exit(1)

            finally:
                if con:
                    con.close()
        else:
            print error_message + "Proper arguments not fulfilled."
            sys.exit(1)

    def version():
        print ver
