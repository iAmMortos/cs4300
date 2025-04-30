"""
Sure! Here’s a functional-style XML parser in Python that mimics the functionality of your original object-oriented version but uses pure functions, immutable data, and namedtuples (or dataclass(frozen=True) if preferred) instead of classes with mutable state.

It will:
	•	Parse simple XML
	•	Return a tree of elements with tag names, children, and text
	•	Allow querying elements by tag
	•	Handle basic text nodes and self-closing tags
	•	Avoid side effects (like mutation or global state)

⸻
"""
"""
Functional XML Parser
"""

import re
from collections import namedtuple
from typing import List, Union, Optional

XmlElement = namedtuple('XmlElement', ['tag', 'children', 'text'])
TextNode = namedtuple('TextNode', ['text'])

# Regex-based tag extraction
def tag_iter(xml):
    tag_pattern = re.compile(r"(<\/?([^/>]+)>|<([^/>]+)\/>)")
    for match in tag_pattern.finditer(xml):
        full_tag = match.group(0)
        tagname = match.group(2) or match.group(3)
        span = match.span()
        if full_tag.startswith('<?'):
            tag_type = 'meta'
        elif full_tag.endswith('/>'):
            tag_type = 'selfclose'
        elif full_tag.startswith('</'):
            tag_type = 'close'
        else:
            tag_type = 'open'
        yield {
            'type': tag_type,
            'tag': tagname.strip(),
            'start': span[0],
            'end': span[1]
        }

# Recursive XML parser
def parse_xml(xml: str) -> XmlElement:
    tags = list(tag_iter(xml))
    if not tags:
        raise ValueError("No tags found")

    root_tag = tags[0]
    end_tag = tags[-1]
    if root_tag['tag'] != end_tag['tag']:
        raise ValueError("Mismatched root tags")

    body = xml[root_tag['end']:end_tag['start']]
    children = parse_children(body)
    return XmlElement(tag=root_tag['tag'], children=children, text=None)

def parse_children(xml: str) -> List[Union[XmlElement, TextNode]]:
    children = []
    tagstack = []
    parse_idx = 0

    for tag in tag_iter(xml):
        text = xml[parse_idx:tag['start']].strip()
        if text and not tagstack:
            children.append(TextNode(text))

        if tag['type'] == 'open':
            tagstack.append(tag)
        elif tag['type'] == 'close':
            if not tagstack:
                continue  # malformed
            opentag = tagstack.pop()
            if opentag['tag'] == tag['tag'] and not tagstack:
                segment = xml[opentag['start']:tag['end']]
                children.append(parse_xml(segment))
        elif tag['type'] == 'selfclose' and not tagstack:
            selfclose_xml = xml[tag['start']:tag['end']]
            children.append(XmlElement(tag=tag['tag'], children=[], text=None))
        
        parse_idx = tag['end']

    trailing = xml[parse_idx:].strip()
    if trailing:
        children.append(TextNode(trailing))

    return children

# Query helpers
def get_children_by_tag(element: XmlElement, tag: str) -> List[XmlElement]:
    return [child for child in element.children if isinstance(child, XmlElement) and child.tag == tag]

def get_first_by_tag(element: XmlElement, tag: str) -> Optional[XmlElement]:
    for child in element.children:
        if isinstance(child, XmlElement) and child.tag == tag:
            return child
    return None

def get_value(element: XmlElement) -> Optional[str]:
    text_nodes = [c for c in element.children if isinstance(c, TextNode)]
    if len(element.children) == 1 and text_nodes:
        return text_nodes[0].text
    elif not element.children:
        return ""
    return None
    
"""
⸻

Advantages of the Functional Approach
	•	Immutability: No mutable state — everything is created anew.
	•	Testable and composable: Small pure functions are easier to reason about.
	•	Predictable: Easier to debug than mutable class hierarchies.

⸻

Would you like this version to support attributes or more complex queries (e.g., XPath-like filters)?
"""
