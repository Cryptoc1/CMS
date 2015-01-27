#!/usr/bin/env python
import MySQLdb as mdb
import sys

ver = "0.0.0b"
error_message = "There was an error when attempting to process your request. System returned:\n"
no_res = "No results  found, response from server: "
no_args = "Proper arguments not fulfilled."

class CMS:
    def __init__(self, hostname, username, password, db):
        self.hostname = hostname
        self.username = username
        self.password = password
        self.db = db

    def connect(self):
        return mdb.connect(self.hostname, self.username, self.password, self.db)

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
            con = self.connect()
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
            con = self.connect()
            cur = con.cursor()
            cur.execute("SELECT * FROM Posts;")

            res = cur.fetchall()
            if res == None:
                return error_message + no_res
            else:
                posts = []
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
                con = self.connect()
                cur = con.cursor()
                cur.execute(req)

                res = cur.fetchone()
                if res == None:
                    return error_message + no_res
                else:
                    p = {}
                    p["pid"] = res[0]
                    p["title"] = res[1]
                    p["author"] = res[2]
                    p["content"] = res[3]

                    return p

            except mdb.Error, e:
                print error_message + str(e)
                sys.exit(1)
            finally:
                if con:
                    con.close()
        else:
            print error_message + no_args
            sys.exit(1)

    def get_posts_by_title(self, title):
        if title:
            req = "SELECT * FROM Posts WHERE title=\"" + title + "\";"
            try:
                con = self.connect()
                cur = con.cursor()
                cur.execute(req)

                res = cur.fetchall()
                if res == None:
                    return error_mesage + no_res
                else:
                    posts = []
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
        else:
            print error_message + no_args
            sys.exit(1)

    def get_posts_by_author(self, author):
        if author:
            req = "SELECT * FROM Posts WHERE author=\"" + author + "\";"
            try:
                con = self.connect()
                cur = con.cursor()
                cur.execute(req)

                res = cur.fetchall()

                if res == None:
                    return error_message + no_res
                else:
                    posts = []
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
        else:
            print error_message + no_args
            sys.exit(1)

    def new_post(self, title, author, content):
        if title and author and content:
            req = "INSERT INTO Posts (title, author, content) VALUES (\""  + str(title) + "\", \"" + str(author) + "\", \"" + str(content) + "\");"
            try:
                con = self.connect()
                cur = con.cursor()
                cur.execute(req)
                con.commit()

                return True

            except mdb.IntegrityError or mdb.Error, e:
                print error_message + str(e)
                sys.exit(1)
                return False

            finally:
                if con:
                    con.close()
        else:
            print error_message + no_args
            sys.exit(1)
            return False

    def update_post_title(self, pid, new_title):
        if new_title:
            req = "UPDATE Posts SET title=\"" + new_title + "\" WHERE pid=\"" + str(pid) + "\";" 
            try:
                con = self.connect()
                cur = con.cursor()
                cur.execute(req)
                con.commit()

                return True

            except mdb.IntegrityError or mdb.Error, e:
                print error_message + str(e)
                sys.exit(1)
                return False

            finally:
                if con:
                    con.close()
        else:
            print error_message + no_args
            sys.exit(1)
            return False

    def update_post_author(self, pid, new_author):
        if new_author:
            req = "UPDATE Posts SET author=\"" + new_author + "\" WHERE pid=\"" + str(pid) + "\";"
            try:
                con = self.connect()
                cur = con.cursor()
                cur.execute(req)
                con.commit()

                return True
            
            except mdb.IntegrityError or mdb.Error, e:
                print error_message + str(e)
                sys.exit(1)
                return False

            finally:
                if con:
                    con.close()
        else:
            print error_message + no_args
            sys.exit(1)
            return False

    def update_post_content(self, pid, new_content):
        if new_content:
            req = "UPDATE Posts SET content=\"" + new_content + "\" WHERE pid=\"" + str(pid) + "\";"
            try:
                con = self.connect()
                cur = con.cursor()
                cur.execute(req)
                con.commit()

                return True
            
            except mdb.IntegrityError or mdb.Error, e:
                print error_message + str(e)
                sys.exit(1)
                return False

            finally:
                if con:
                    con.close()
        else:
            print error_message + no_args
            sys.exit(1)
            return False

    def version():
        print ver
