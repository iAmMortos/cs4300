
import io
import xml.etree.ElementTree as ET

# Load and parse XML
def parse_xml(xml_string):
    root = ET.fromstring(xml_string)
    books = []
    
    # Step through each book and extract relevant data
    for book in root.findall('book'):
        title = book.find('title').text
        author = book.find('author').text
        books.append(f"{title} by {author}")
    
    return books

# Sample XML string
xml_data = ''
with io.open('../rsc/books.xml') as f:
  xml_data = f.read()
book_list = parse_xml(xml_data)

# Print result
for book in book_list:
    print(book)
    
