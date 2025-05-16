
from xmelement import Xmelement
import io

def bonus_for(score):
  bonus = (int(score) - 10) // 2
  return f"{'+' if bonus >= 0 else ''}{bonus}"

def make_bonus_str(score):
  return f'{score} ({bonus_for(score)})'

def main():
  monster = Xmelement.load_from_file("../rsc/monsters/Goblin.xml")
  print(monster.get("name").value)
  trait = monster.get("trait")
  print(f'  {trait.get("name").value}. {trait.get("text").value}')
  print(f'\tSTR   \tDEX   \tCON   \tINT   \tWIS   \tCHA\n\t{make_bonus_str(monster.get("str").value)}\t{make_bonus_str(monster.get("dex").value)}\t{make_bonus_str(monster.get("con").value)}\t{make_bonus_str(monster.get("int").value)}\t{make_bonus_str(monster.get("wis").value)}\t{make_bonus_str(monster.get("cha").value)}')
  actions = monster.getall("action")
  for action in actions:
    print(action.get("name").value)
    print(action.get("text").value)
    print(action.get("attack").value)
    
  # print(monster.get("description").value)

if __name__ == '__main__':
  main()

"""
This custom XML parser is a clever minimalist implementation, but there are several points to address in terms of efficiency, ease of use, and robustness.

⸻

1. Efficiency

Pros:
	•	Uses regular expressions for lightweight tag matching, which avoids the overhead of full DOM parsing.
	•	Minimal object construction; only builds tree structure as needed.

Cons:
	•	Regex-based XML parsing is error-prone and potentially inefficient for large or complex XML documents. XML is not a regular language; regex can’t reliably handle edge cases like nested tags, attributes, CDATA, or namespaces.
	•	Tag stack management in _parse is linear and should be performant for simple, shallow structures, but could degrade on deeply nested XML.
	•	No caching or optimization techniques like memoization or iterative parsing for very large files.

⸻

2. Ease of Use

Pros:
	•	value, tagname, and get(tag) provide a convenient interface for simple XML structures.
	•	Recursively creates child Xmelement objects for nested parsing—nice for hierarchical access.

Cons:
	•	get(tag) returns Xmelement, None, or List[Xmelement] depending on count. This overloading return type is convenient but may lead to bugs or extra type() checking for users.
	•	Suggestion: separate methods like get_first(tag) and get_all(tag) would be more intuitive and safe.
	•	load_from_file() assumes a UTF-8 encoded file and returns an Xmelement marked as root—solid, but lacks options for alternate encodings or error handling.
	•	No support for attributes in tags, which is a significant limitation for general XML use.
	•	Minimal error handling: # pass # error indicates a lot of missing robustness for malformed XML.

⸻

3. Code Structure & Maintainability

Pros:
	•	Clear modular methods for _parse, _preprocess_xml, etc.
	•	Logical object-oriented design.

Cons:
	•	_TextNode should probably be part of a shared base class/interface with Xmelement to allow uniform tree traversal.
	•	Tight coupling to XmlTag class, which we can’t evaluate here, but is critical to correctness. If XmlTag doesn’t robustly distinguish tag types, things break silently.

⸻

Suggestions for Improvement
	1.	Return Types: Refactor get() into more predictable variants.
	2.	Error Handling: Replace # pass # error with proper exceptions.
	3.	Support Attributes: Add parsing logic for tag attributes if XmlTag doesn’t already.
	4.	Validation: Add optional XML schema validation or well-formedness checks.
	5.	Unit Tests: Add unit tests to confirm edge case behavior (unclosed tags, nested tags, etc.).
	6.	Performance Profiling: If used on large files, consider streaming/token-based parsing instead.

⸻

Final Verdict
	•	Great for simple XML structures or specific domains where XML is highly predictable (e.g., game data, config files).
	•	Not suitable as a general-purpose XML parser. For general use, Python’s xml.etree.ElementTree or lxml are more robust.

Let me know if you’d like a refactored or enhanced version based on your use case!
"""
