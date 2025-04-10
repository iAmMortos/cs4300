
import io
import xml.etree.ElementTree as ET

# Load and parse XML
def parse_monster(xml_string):
    root = ET.fromstring(xml_string)
    
    # Step through each book and extract relevant data
    name = root.find("name").text
    size = root.find("size").text
    creature_type = root.find("type").text
    alignment = root.find("alignment").text
    
    ac = root.find("ac").text
    hp = root.find("hp").text
    speed = root.find("speed").text
    stats = {
      "STR": root.find("str").text,
      "DEX": root.find("dex").text,
      "CON": root.find("con").text,
      "INT": root.find("int").text,
      "WIS": root.find("wis").text,
      "CHA": root.find("cha").text
    }
    
    return {
      "Name": name,
      "Size": size,
      "Type": creature_type,
      "Alignment": alignment,
      "AC": ac,
      "HP": hp,
      "Speed": speed,
      "Stats": stats,
    }


if __name__ == '__main__':  
  # Sample XML string
  xml_data = ''
  with io.open('../rsc/monsters/Goblin.xml') as f:
    xml_data = f.read()
  monster = parse_monster(xml_data)
  
  for key, value in monster.items():
    print(f"{key}: {value}")
    
