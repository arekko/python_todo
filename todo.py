from datetime import date
from datetime import time
from datetime import datetime
import mysql.connector


db = mysql.connector.connect(user='todo',
                             password='todo',
                             host='localhost',
                             database='tododb')

#main part
def main():
    guideFunc()

    menu = ""

    while menu != "e":
        # menu = input("Enter the command: ")
        if menu == "show" or menu == "s":
            showItems() 
        elif menu == "new" or menu == "n":
            getNotes()
        elif menu == "d":
            delI = int(input("Enter note id, which you want to delete: "))
            delItem(delI)
        elif menu =="h":
            guideFunc()
        menu = input("Enter the command: ")
        # else:
        #     print("Incorrect command! Try again")


    # printFunc()
    db.close()


def guideFunc():
    print("This is console simple note. Press 'n' to add new note, 's' to show all notes, 'del' to delete the note, 'e' to exit from app, 'h' to show advice)")

def getNotes():
    title_var = input("Write a title: ")
    note_var = input("Write a notes: ")

    getFunc(title_var, note_var)

def delItem(delNote):
    cur = db.cursor()
    sql = "DELETE FROM todo WHERE ID = '%i'" % (delNote)
    cur.execute(sql)
    db.commit()


def getFunc(title, art):
    # title = "Email"
    # art = "I need to send email"
    cur = db.cursor()
    sql = "INSERT INTO todo VALUES(NULL, '%s', '%s')" % (title , art)
    cur.execute(sql)
    db.commit()


def showItems():
    cur = db.cursor()
    sql = "SELECT * FROM todo"
    cur.execute(sql)
    rez = cur.fetchall()

    for i in rez:
        print("# " + str(i[0]), end=" ")
        print(str(i[1]), end="  ")
        print(" - " + str(i[2]))

    return


if __name__== "__main__":
    main()
