
import xml.etree.ElementTree as ET
import io
from typing import List

# Pure function to extract books from XML
def parse_xml(xml_string: str) -> List[str]:
    root = ET.fromstring(xml_string)
    return [f"{book.find('title').text} by {book.find('author').text}"
            for book in root.findall('book')]

# Sample XML string
with io.open('../rsc/books.xml') as f:
  xml_data = f.read()
book_list = parse_xml(xml_data)

# Print result
for book in book_list:
    print(book)
    
