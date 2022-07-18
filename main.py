import pickle
import csv
import time



def get_book_info(search_term_group='', search_term=''):
    if search_term_group == "" or search_term == "":
        search_term_group = input("\nbookID(1) / bookname(2) / author name(3) / genre(4) / stack number(5) / publisher(6) : ")
        search_term = input("\nenter the term : ")
    if search_term_group == "" or search_term == "":
        return "no input"
    f = open("bookslist.csv", "r")
    content = list(csv.reader(f))
    f.close()
    del f
    if search_term_group in ["bookID", "bookid", "1"]:
        for i in content:
            if i[0] == search_term:
                return i
    elif search_term_group in ["bookname", "2"]:
        retun_list = []
        for i in content:
            if search_term in i[1]:
                return_list.append(i)
        return return_list
    elif search_term_group in ["author name", "authorname", "author", "3"]:
        retun_list = []
        for i in content:
            if search_term in i[2]:
                return_list.append(i)
        return return_list
    elif search_term_group in ["genre", "4"]:
        retun_list = []
        for i in content:
            if search_term in i[3]:
                return_list.append(i)
        return return_list
    elif search_term_group in ["stack number", "stacknumber", "stack", "5"]:
        for i in content:
            if i[4] == search_term:
                return i
    elif search_term_group in ["publisher", "6"]:
        return_list = []
        for i in content:
            if search_term in i[5]:
                return_list.append(i)
        return return_list
    else:
        time.sleep(2)
        return "invalid input"



def get_student_info(given_info_group = input("\n rollno(1) / name(2) / dept(3) / return bookID(4) : "), given_info = input("\nenter the info : ")):
    if given_info == "" or given_info_group == "":
        given_info_group = input("\n rollno(1) / name(2) / dept(3) / return bookID(4) : ")
        given_info = input("\nenter the info : ")
    if given_info == "" or given_info_group == "":
        return "no input"
    f = open("studentlist.csv", "r")
    student_info = list(csv.reader(f))  # rno, name, g, course, dept, sec(A/B/N)
    f.close()
    f = open("lendinglist.csv", "r")    # roll no, date (yyyymmdd), time(2460)
    lending_history = list(csv.reader(f))
    f.close()
    del f
    if given_info_group in ["rollno", "roll no", "r no", "rno", "1"]:
        for i in student_info:
            if i[0] == given_info:
                return i
    elif given_info_group in ["name", "2"]:
        return_list = []
        for i in student_info:
            if given_info in i[1]:
                return_list.append(i)
        return return_list
    elif given_info_group in ["dept", "department", "dpt", "3"]:
        return_list = []
        for i in student_info:
            if given_info in i[4]:
                return_list.append(i)
        return return_list
    elif given_info_group in ["bookID", "returnbookid", "bookid", "return bookID", "4"]:
        return_list = []
        for i in lending_history:
            if i[3] == given_info:
                return_list.append(i)
        return return_list
    else:
        time.sleep(2)
        return "invalid input"


while True:
    search_term_group = input("\nbookID(1) / bookname(2) / author name(3) / genre(4) / stack number(5) / publisher(6) : ")
    search_term = input("\nenter the term : ")
    print(get_student_info(search_term_group, search_term))