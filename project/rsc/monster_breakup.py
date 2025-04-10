import xml.etree.ElementTree as ET
import xml.dom.minidom
import io

def to_xml_str(node):
    xml_str = ET.tostring(node, encoding='utf-8').replace(b'\n', b'')
    dom = xml.dom.minidom.parseString(xml_str)
    s = dom.toprettyxml()
    return s

def main():
  tree = ET.parse('bestiary-mm.xml')
  root = tree.getroot()
  for e in root:
    if e.tag == "monster":
      nametag = e.find('name')
      name = nametag.text
      filename = 'monsters/' + name.replace(' ', '_').replace('(', '').replace(')', '').replace("'", '') + '.xml'
      with io.open(filename, 'w', encoding="utf-8") as f:
        f.write(to_xml_str(e))
    else:
      print("Non-monster tag:", e.tag)
  print('Done.')
  

if __name__ == '__main__':
  main()
  
