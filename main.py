#!/usr/bin/env python
from CMS import CMS
import sys

manager = CMS(hostname="localhost", username="test", password="test123", db="CMS")

tchar = ": "
working = tchar + "Working..."

def verify_input(cmd):
    new_cmd = str(cmd).lower()
    if new_cmd == "exit":
        print tchar + "Exiting CMS..."
        sys.exit()
    elif new_cmd == "help":
        # TODO: make help pages
        print tchar
        main()
    else:
        if new_cmd not in commands:
            default()
        else:
            commands[new_cmd]()

def get_post():
    print tchar + "Select by pid, title, or author?"
    method = str(raw_input(tchar)).lower()
    if method == "pid":
        print tchar + "Enter Post ID (pid)"
        pid = raw_input(tchar)
        try:
            pid = int(pid)
        except ValueError:
            print tchar+ "Value entered was not a number."
            get_post()
        print working
        post = manager.get_post_by_id(pid)
        print organize_post_data(post)
        main()
    elif method == "title":
        print tchar + "Enter Post Title (title)"
        title = str(raw_input(tchar))
        print working
        posts = manager.get_posts_by_title(title)
        print organize_post_data(posts)
        main()
    elif method == "author":
        print tchar + "Enter Post Author (author)"
        author = str(raw_input(tchar))
        print working
        posts = manager.get_posts_by_author(author)
        print organize_post_data(posts)
        main()
    elif method != "pid" and method != "title" and method != "author":
        print "Invalid Selection Method."
        get_post()

def get_all():
    count = manager.get_entry_count()
    if count == 1:
        print tchar + "There is " + str(count) + " total entry.\n" + tchar + "Are you sure you want to list them all? (y/n)"
    else:
        print tchar + "There is " + str(count) + " total entries\n" + tchar + "Are you sure you want to list them all? (y/n)"
    choice = raw_input(tchar).lower()
    if choice == "y":
        print working
        print organize_post_data(manager.get_all_posts())
        main()
    elif choice == "n":
        print tchar + "Okay, exiting \"get all\" command."
        main()
    else:
        print tchar + "There was an error... Exiting \"get all\" command."
        main()

def new_post():
    print tchar + "Your are about to create a new post! A series of prompts are going to ask you to enter some information.\n Continue? (y/n)"
    choice = raw_input(tchar).lower()
    if choice == "y":
        print tchar + "Enter the title of this Post"
        title = raw_input(tchar + "\ttitle: ")
        print tchar + "Enter author of this Post"
        author = raw_input(tchar + "\tauthor: ")
        print tchar + "Enter absolute path to markdown file"
        content = raw_input(tchar + "\tpath to md: ")
        
        # TODO: Load text from md file

    elif choice == "n":
        print tchar + "Okay, exiting \"new post\" command."
        main()
    else:
        print tchar + "There was an error... Exiting \"new post\" command."
        main()

# TODO: create update post function
'''
def update_title():

def update_author():

def update_content();

'''

def default():
    print tchar + "Unrecognized command, please try again."
    main()

commands = {
        "get post": get_post,
        "get all": get_all,
        "new post": new_post
        }

def organize_post_data(post_data):
    post_as_string = ""
    print tchar +  "The content property is returned as inline markdown,\n" + tchar + "meaning escape characters (\\n, \\t, etc.) will be processed."
    if type(post_data) == list:
        for i in post_data:
            post_as_string += "{\n\t \"pid\": " + str(i["pid"]) + "\n\t \"title\": \"" + i["title"] + "\"\n\t \"author\": \"" + i["author"] + "\"\n\t \"content\": \"" + i["content"]+ "\"\n}"
    else:
        post_as_string = "{\n\t \"pid\": " + str(post_data["pid"]) + "\n\t \"title\": \"" + post_data["title"] + "\"\n\t \"author\": \"" + post_data["author"] + "\"\n\t \"content\": \"" + post_data["content"]+ "\"\n}"

    return post_as_string


def main():
    cmd = raw_input(tchar)
    verify_input(cmd)

print tchar + "Starting CMS..."
print tchar + "To exit, type 'exit'. To view more commands, type 'help'."
print tchar + "Enter a command to begin."
main()
