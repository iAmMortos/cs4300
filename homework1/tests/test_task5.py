
import context
import task5
from errors.malformed_csv import MalformedCSVException, BadCSVRowException
import pytest


def test_load_csv_as_table():
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
  bl = task5.BookList
  
  
def test_BookList_print_n_books():
  pass
  
  
def test_Student():
  pass
  
  
def test_StudentDB():
  pass
  
  
def test_StudentDB_get_student():
  pass
  
  
# def

