import csv
import io
import os
from errors.malformed_csv import MalformedCSVException, BadCSVRowException


"""
Loads an entire CSV file into a table (not good for large CSVs)

Parameters:
  csv_path: path to the csv file to open.
  delimiter: passed to csv reader. Default ','
  quotechar: passed to csv reader. Default '"'
  numcols: (optional) If provided, will validate that all the rows returned
    from the csv reader are of the given length. 
    If not provided, this will not be enforced.
    
Throws:
  FileNotFoundError - if csv_path is invalid
  MalformedCSVException - If numcols is provided and the length of any row 
    in the CSV does not match numcols.
    
Returns: A table of string values loaded from the given CSV file.
"""
def load_csv_as_table(csv_path, delimiter=',', quotechar='"', numcols=None):
  data_table = []
  if not os.path.exists(csv_path):
    raise FileNotFoundError(f"The csv file [{csv_path}] does not exist.")
  with io.open(csv_path, encoding="utf-8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=delimiter, quotechar=quotechar)
    for row in csvreader:
      if numcols:
        if len(row) != numcols:
          raise MalformedCSVException(f"A row of the CSV did not match the given numcols value [{numcols}]. {row}.")
      data_table += [row]
    return data_table


"""
Represents a book with a title and an author.

Parameters:
  csvrow - a list or tuple of length 2.
    e.g. ["The Bible", "God"]
"""
class Book(object):
  def __init__(self, csvrow):
    # Unpack csvrow items into member variables
    self.title, self.author = csvrow
  def __repr__(self):
    return f"Title: {self.title}, Author: {self.author}"
    

"""
Represents a list of Book objects.

Parameters:
  booklist_path - The path to the booklist CSV file. Must be a
    CSV file with exactly 2 columns.
"""
class BookList(object):
  def __init__(self, booklist_path):
    self._books = []
    table = load_csv_as_table(booklist_path, numcols=2)
    for row in table:
      self._books.append(Book(row))
      
  # Prints the first n books in the list
  def print_n_books(self, n):
    print('\n'.join([str(b) for b in self._books[:n]]))
  

"""
Represents a student with a first and last name, and a student ID.

Parameters:
  csvrow - a list or tuple of length 3. The 3rd item must be parsable 
    as an integer.
    e.g. ["Taylor", "Lopez", "5"]
    
Throws:
  BadCSVRowException - If the third value in the row list isn't 
    parsable as an integer.
"""
class Student(object):
  def __init__(self, csvrow):
    self.id, self.first_name, self.last_name = csvrow
    self.id = int(self.id)
    
  def __repr__(self):
    return f"{self.first_name} {self.last_name} ({self.id})"
    
    
"""
Represents a "database" of Students stored by their student ID.

Parameters:
  studentlist_path: the path to the studentlist CSV file. Must be
    CSV file with exactly 3 columns.
"""
class StudentDB(object):
  def __init__(self, studentlist_path):
    self._db = {}
    table = load_csv_as_table(studentlist_path, numcols=3)
    for row in table:
      student = Student(row)
      self._db[student.id] = student
  
  def get_student(self, id):
    return self._db[id]
    

if __name__ == '__main__':
  print("Printing my 3 favorite books:")
  my_books = BookList('rsc/task5_books.csv')
  my_books.print_n_books(3)
  
  print()
  
  print("Getting Student No. 2")
  student_db = StudentDB('rsc/task5_students.csv')
  print(student_db.get_student(2))
  
  
