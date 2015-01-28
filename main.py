#!/usr/bin/env python
from CMS import CMS
import sys
import os

manager = CMS(hostname="localhost", username="test", password="test123", db="CMS")

tchar = ": "
working = tchar + "Working..."

def verify_input(cmd):
    new_cmd = str(cmd).lower()
    if new_cmd == "exit":
        print tchar + "Exiting CMS..."
        sys.exit()
        os.system("clear")
    elif new_cmd == "help":
        print tchar + "\n" + tchar + "clear :: Clear the screen\n" + tchar + "exit :: Exit the program\n"  + tchar + "help :: Display this help text"
        print tchar + "get <arg>\n" + tchar + "\tall :: Display all entries\n" + tchar + "\tpost :: Display entry that matches specified Selection Query"
        print tchar + "new <arg>\n" + tchar + "\tpost :: Create a new entry"
        print tchar + "update <arg>\n" + tchar + "\tpost :: Update specified feilds of an entry"
        print tchar + "delete <arg>\n" + tchar + "\tpost :: Delete an entry"
        print tchar
        main()
    elif new_cmd == "clear":
        os.system("clear")
        main()
    elif new_cmd == "get":
        print tchar + "Get what?\n" + tchar + "\tget <arg>\n" + tchar + "\t\tall :: Display all entries\n" + tchar + "\t\tpost :: Display entry that matches specified Selection Query"
        main()
    elif new_cmd == "new":
        print tchar + "New what?\n" + tchar + "\tnew <arg>\n" + tchar + "\t\tpost :: Create a new entry"
        main()
    elif new_cmd == "update":
        print tchar + "Update what?\n" + tchar + "\tupdate <arg>\n" + tchar + "\t\tpost :: Update specified feilds of an entry"
        main()
    elif new_cmd == "delete":
        print tchar + "Delete what?\n" + tchar + "\tdelete <arg>\n" + tchar + "\t\tpost :: Deletes an entry"
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
        print tchar + "There are " + str(count) + " total entries\n" + tchar + "Are you sure you want to list them all? (y/n)"
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
        print tchar + "Enter path to markdown file"
        path = raw_input(tchar + "\tpath to md: ")
        f = open(path, 'r')
        content = f.read()
        print tchar + "You are about to create the post " + title + ". \n Continue? (y/n)"
        choice = raw_input(tchar).lower()
        if choice == "y":
            print working
            if manager.new_post(title, author, content):
                f.close()
                print tchar + "New Post created. To view it, use \"get post\" with pid: " + str(manager.get_entry_count())
                main()
            else:
                print tchar + "Failed to create new post."
                main()
        elif choice == "n":
            print tchar + "Okay, exiting \"new post\" command."
        else:
            print tchar + "There was an error... Exiting \"new post\" command."

    elif choice == "n":
        print tchar + "Okay, exiting \"new post\" command."
        main()
    else:
        print tchar + "There was an error... Exiting \"new post\" command."
        main()

def update_post():
    print tchar + "You're about to update a post! A series of prompts will ask you for update information.\n Continue? (y/n)"
    choice = raw_input(tchar).lower()
    if choice == "y":
        print tchar + "Enter the Post ID (pid) of the post to update"
        pid = raw_input(tchar)
        print tchar + "What attribute do you want to update: title, author, or content?"
        attr = raw_input(tchar).lower()
        if attr == "title":
            print tchar + "Enter the new title for Post with pid: " + str(pid)
            title = raw_input(tchar + "\ttitle: ")
            print tchar + "You are about to update Post with pid: " + str(pid) + " with the new title:\"" + title + "\". \nContinue? (y/n)"
            choice = raw_input(tchar).lower()
            if choice == "y":
                print working
                if manager.update_post_title(pid, title):
                    print tchar + "Updated post. Use \"get post\" with pid: " + str(pid) + " to view changes."
                    main()
                else:
                    print tchar + "Failed to update post."
            elif choice == "n":
                print tchar + "Okay, exiting \"update post\" command."
                main()
            else:
                print tchar + "There was an error... Exiting \"update post\" command."
                main()  
        elif attr == "author":
            print tchar + "Enter the new author for Post with pid: " + str(pid)
            author = raw_input(tchar + "\tauthor: ")
            print tchar + "You are about to update Post with pid: " + str(pid) + " with the new author:\"" + author + "\". \nContinue? (y/n)"
            choice = raw_input(tchar).lower()
            if choice == "y":
                print working
                if manager.update_post_author(pid, author):
                    print tchar + "Updated post. Use \"get post\" with pid: " + str(pid) + " to view changes."
                    main()
                else:
                    print tchar + "Failed to update post."
            elif choice == "n":
                print tchar + "Okay, exiting \"update post\" command."
                main()
            else:
                print tchar + "There was an error... Exiting \"update post\" command."
                main()  
        elif attr == "content":
            print tchar + "Enter the path to the markdown file containing the new post content for post with pid: " + str(pid)
            path = raw_input(tchar + "\tpath to md: ")
            f = open(path, 'r')
            content = f.read()
            print tchar + "You are about to update Post with pid: " + str(pid) + " with the new content.\nContinue? (y/n)"
            choice = raw_input(tchar).lower()
            if choice == "y":
                print working
                if manager.update_post_content(pid, content):
                    f.close()
                    print tchar + "Post content updated. Use \"get post\" with pid: " + str(pid) + " to view changes."
                    main()
                else:
                    print thcar + "Failed to update content."
                    main()
            elif choice == "n":
                print tchar + "Okay, exiting \"update post\" command."
                main()
            else:
                print tchar + "There was an error... Exiting \"update post\" command."
                main()
        elif attr != "title" or attr != "author" or attr != "content":
            print tchar + "Invalid attribute."
            update_post()
    elif choice == "n":
        print tchar + "Okay, exiting \"update post\" command."
        main()
    else:
        print tchar + "There was an error... Exiting \"update post\" command."
        main()

def delete_post():
    print tchar + "You are about to delete a post! This action can not be reversed. \nContinue? (y/n)"
    choice = raw_input(tchar).lower()
    if choice == "y":
        print tchar + "Enter Post ID (pid) of post to delete"
        pid = raw_input(tchar)
        print tchar + "Are you sure you want to delete Post with pid:\"" + str(pid) + "\"? (y/n)"
        choice = raw_input(tchar)
        if choice == "y":
            if manager.remove_post(pid):
                print tchar + "Post with pid:\"" + str(pid) + "\" deleted."
                main()
            else:
                print tchar + "Failed to delete post."
                main()
        elif choice == "n":
            print tchar + "Okay, exiting \"delete post\" command."
            main()
        else:
            print tchar + "There was an error... Exiting \"delete post\" command."
            main()

    elif choice == "n":
        print tchar + "Okay, exiting \"delete post\" command."
        main()
    else:
        print tchar + "There was an error... Exiting \"delete post\" command."
        main()

def default():
    print tchar + "Unrecognized command, please try again."
    main()

commands = {
        "get post": get_post,
        "get all": get_all,
        "new post": new_post,
        "update post": update_post,
        "delete post": delete_post
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

os.system("clear")
print tchar + "Starting CMS..."
print tchar + "To exit, type 'exit'. To view more commands, type 'help'."
print tchar + "Enter a command to begin."
main()
