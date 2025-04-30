
from func_xml import *
import io

with io.open("../rsc/monsters/Goblin.xml") as f:
  xml = f.read()
parsed = parse_xml(xml)

print(parsed.tag)  # 'root'
print(get_value(get_first_by_tag(parsed, 'hp')))  # '10'
print(get_value(get_first_by_tag(parsed, 'name')))  # 'Goblin'
print(get_value(get_first_by_tag(parsed, 'empty')))  # ''

