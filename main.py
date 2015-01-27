#!/usr/bin/env python
from CMS import CMS
import json
import sys

manager = CMS(hostname="localhost", username="test", password="test123", db="CMS")

tchar = ": "
working = tchar + "Working..."

def verify_input(cmd):
    new_cmd = str(cmd).lower()
    if new_cmd == "exit":
        print tchar + "Exiting CMS..."
        sys.exit()
    else:
        if new_cmd not in commands:
            default()
        else:
            commands[new_cmd]()

def get_post():
    print tchar + "How should Posts by found? By pid, title, or author?"
    method = str(raw_input(tchar)).lower()
    if method == "pid":
        print tchar + "Enter Post ID (pid)"
        pid = int(raw_input(tchar))
        print working
        post = manager.get_post_by_id(pid)
        print tchar + "{"
        print tchar + "\t \"pid\": \"" + str(post["pid"]) + "\""
        print tchar + "\t \"title\": \"" + post["title"] + "\""
        print tchar + "\t \"author\": \"" + post["author"] + "\""
        print tchar + "\t \"content\": \"" + post["content"]+ "\""
        print tchar + "}"
        main()
    if method == "title":
        print tchar + "Enter Post Title (title)"
        title = str(raw_input(tchar))
        print working
        posts = manager.get_posts_by_title(title)
        print tchar + str(posts)
        main()
    if method == "author":
        print tchar + "Enter Post Author (author)"
        author = str(raw_input(tchar))
        print working
        posts = manager.get_posts_by_author(author)
        print tchar + str(posts)
        main()

def default():
    print tchar + "Unrecognized command, please try again."
    main()

commands = {
        "get post": get_post
}

def main():
    cmd = raw_input(tchar)
    verify_input(cmd)

print tchar + "Starting CMS..."
print tchar + "Enter a command to begin."
main()
