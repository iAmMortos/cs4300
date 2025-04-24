
from xmelement import Xmelement
import io

def main():
  monster = Xmelement.load_from_file("../rsc/monsters/Goblin.xml")
  print(monster.get("name").value)
  trait = monster.get("trait")
  print(trait.get("name").value)
  print(trait.get("text").value)
  
  actions = monster.get("action")
  for action in actions:
    print(action.get("name").value)
    print(action.get("text").value)
    print(action.get("attack").value)

if __name__ == '__main__':
  main()

