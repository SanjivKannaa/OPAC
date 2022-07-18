import pickle
import csv
import time



def get_book_info(search_term_group = input("\nbookID(1) / bookname(2) / author name(3) / genre(4) / stack number(5) / publisher(6) : "), search_term = input("\nenter the term : ")):
    content = list(csv.reader(open("bookslist.csv", "r")))
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
        return "wrong input for group"



print(get_book_info())