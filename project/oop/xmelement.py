
import re
import io
from xmltag import XmlTag

class Xmelement (object):
  def __init__(self, xml, is_root=False):
    tags = list(Xmelement._tag_iter(xml))
    self._is_root = is_root
    self._children = []
    self._inner_text = ""
    self._tag = None
    
    # strip meta and parent tag
    xml = self._preprocess_xml(tags, xml)
    
    self._metatag = None
    self._parse(xml)
    
  """
  Nice way to return a single value from an xml node if it's something like
  this: <hp>10</hp>  # returns 10
  or this: <weaknesses></weaknesses>  # returns ""
  otherwise, there isn't a single, clean value; return None
  """
  @property
  def value(self):
    if len(self._children) == 1 and type(self._children[0]) is _TextNode:
      return self._children[0].value
    elif len(self._children) == 0:
      return ""
    else:
      return None
    
  @property
  def tag(self):
    return self._tag
  
  @property
  def tagname(self):
    return self._tag.tag
  
  def getall(self, tagstr):
    found = []
    for child in self._children:
      if child.tagname == tagstr:
        found += [child]
    return found
      
  def get(self, tagstr):
    for child in self._children:
      if child.tagname == tagstr:
        return child
    return None
    
  @staticmethod
  def _tag_iter(xml):
    for match in re.finditer(r"(<\/?([^/>]+)>|<([^/>]+)\/>)", xml):
      yield XmlTag(match.group(0), match.span())
      
  @staticmethod
  def load_from_file(file):
    with io.open(file, encoding="utf-8") as f:
      xml = f.read()
    return Xmelement(xml, is_root=True)
    
  """
  Should determine immediate xml children (not grandchildren or beyond), 
  create Xmelements for them, and pass their responsible xml text. 
  Then those can recursively parse their own xml
  """
  def _parse(self, xml):
    tagstack = []
    parse_idx = 0
    for tag in Xmelement._tag_iter(xml):
      # capture text nodes before next tag
      s = xml[parse_idx:tag.start].strip()
      if s and len(tagstack) == 0:
        self._children.append(_TextNode(s))
      
      if tag.type == "meta":
        self._metatag = tag
      elif tag.type == "open":
        if self._tag is None:
          self._tag = tag
        tagstack.append(tag)
      elif tag.type == "close":
        if tagstack[-1].tag == tag.tag:
          opentag = tagstack.pop()
          if len(tagstack) == 0:
            child_xml = xml[opentag.start:tag.end].strip()
            if child_xml:
              self._children.append(Xmelement(child_xml))
        else:
          # error, tag mismatch
          pass
      elif tag.type == "selfclose":
        if len(tagstack) == 0:
          child_xml = xml[tag.start:tag.end].strip()
          if child_xml:
            self._children.append(Xmelement(child_xml))
      parse_idx = tag.end
      
    if len(tagstack) != 0:
      # xml formatting error - mismatched tags
      pass
    
    s = xml[parse_idx:].strip()
    if s:
      self._children.append(_TextNode(s))
    
  """
  Extract the xml meta tag if it exists.
  Extract the root tag and its info.
  Return all remaining xml text for further parsing
  """
  def _preprocess_xml(self, tags, xml):
    meta = None
    root_open = None
    if tags[0].type == "meta":
      meta = tags[0]
      self._metatag = meta
      root_open = tags[1]
    else:
      root_open = tags[0]
    root_close = tags[-1]
    self._tag = root_open
    
    if root_open.type != "open":
      pass #error
    elif root_close.type != "close":
      pass # error
    elif root_open.tag != root_close.tag:
      pass # error
    
    return xml[root_open.end:root_close.start]
    
    
class _TextNode(object):
  def __init__(self, text):
    self._value = text
  @property
  def value(self):
    return self._value
      
