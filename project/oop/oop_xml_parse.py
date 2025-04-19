
from xmelement import Xmelement
from xml_parser import XmlParser
import io

def load_xml_file(file):
  with io.open(file, encoding="utf-8") as f:
    return Xmelement(f.read())

def main():
  root = load_xml_file("../rsc/monsters/Goblin.xml")

if __name__ == '__main__':
  main()

