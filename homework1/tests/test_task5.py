import sys, os
import context
import task5
from errors.malformed_csv import MalformedCSVException, BadCSVRowException
import pytest


def test_load_csv_as_table():
  context.reset()
  data = task5.load_csv_as_table("rsc/task5_malformed.csv")
  # Just assuring the table loads without complaint
  assert len(data) == 3
  
  with pytest.raises(MalformedCSVException):
    task5.load_csv_as_table("rsc/task5_malformed.csv", numcols=2)
  with pytest.raises(FileNotFoundError):
    task5.load_csv_as_table("rsc/does_not_exist.csv")


def test_Book():
  b = task5.Book(["Cat in the Hat", "Dr. Seuss"])
  assert b.author == "Dr. Seuss"
  assert b.title == "Cat in the Hat"
  

def test_BookList():
  context.reset()
  bl = task5.BookList("rsc/task5_books_good.csv")
  assert len(bl._books) == 5
  assert bl._books[4].title == "Book5"
  assert bl._books[3].author == "Author4"
  
  
def test_BookList_print_n_books(capfd):
  context.reset()
  bl = task5.BookList("rsc/task5_books_good.csv")
  bl.print_n_books(3)
  out, err = capfd.readouterr()
  assert out.strip() == "Title: Book1, Author: Author1\nTitle: Book2, Author: Author2\nTitle: Book3, Author: Author3"
  
  
def test_Student():
  context.reset()
  s = task5.Student(["1","A","B"])

  assert s.id == 1
  assert s.first_name == "A"
  assert s.last_name == "B"

  with pytest.raises(BadCSVRowException):
    task5.Student(["hotdog", "A", "B"])
  
  
def test_StudentDB():
  context.reset()
  sdb = task5.StudentDB("rsc/task5_students_good.csv")
  assert len(sdb._db) == 5
  assert sdb._db[3].first_name == "C"
  assert sdb._db[1].last_name == "AA"
  
  
def test_StudentDB_get_student():
  context.reset()
  sdb = task5.StudentDB("rsc/task5_students_good.csv")
  s1 = sdb.get_student(1)
  assert s1.id == 1
  assert s1.first_name == "A"
  assert s1.last_name == "AA"
  s5 = sdb.get_student(5)
  assert s5.id == 5
  assert s5.first_name == "E"
  assert s5.last_name == "EE"
