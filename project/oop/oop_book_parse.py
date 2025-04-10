
import io
import xml.etree.ElementTree as ET

class Library:
    def __init__(self, xml_string):
        self.root = ET.fromstring(xml_string)

    def get_books(self):
        books = []
        for book in self.root.findall('book'):
            title = book.find('title').text
            author = book.find('author').text
            books.append(f"{title} by {author}")
        return books

# Sample XML string
xml_data = ''
with io.open('../rsc/books.xml') as f:
  xml_data = f.read()
library = Library(xml_data)
book_list = library.get_books()

# Print result
for book in book_list:
    print(book)
    
