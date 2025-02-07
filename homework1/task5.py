import csv
import io

# list of your favorite books (with authors)
# list slicing, print first 3 books in the list.
# create dict represents basic student database
# - student names, student IDs
class Book(object):
  def __init__(self, csvrow):
    # Unpack csvrow items into member variables
    self.title, self.author = csvrow

  def __repr__(self):
    return f"Title: {self.title}, Author: {self.author}"
    
    
class BookList(object):
  def __init__(self, booklist_path):
    self._books = []
    with io.open(booklist_path, encoding="utf-8", newline='') as csvfile:
      csvreader = csv.reader(csvfile, delimiter=',', quotechar='"')
      for row in csvreader:
        self._books.append(Book(row))
      
  def print_n_books(self, n):
    print('\n'.join([str(b) for b in self._books[:n]]))
  

class Student(object):
  def __init__(self, csvrow):
    self.id, self.first_name, self.last_name = csvrow
    self.id = int(self.id)
    
  def __repr__(self):
    return f"{self.first_name} {self.last_name} ({self.id})"
    
    
class StudentDB(object):
  def __init__(self, studentlist_path):
    self._db = {}
    with io.open(studentlist_path, encoding="utf-8", newline='') as csvfile:
      csvreader = csv.reader(csvfile, delimiter=',', quotechar='"')
      for row in csvreader:
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
  
  
