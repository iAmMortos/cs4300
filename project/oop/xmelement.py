
import re
from xmltag import XmlTag

class Xmelement (object):
  def __init__(self, xml, is_root=False):
    self._is_root = is_root
    self._children = []
    self._inner_text = ""
    self._tag = None
    self._parse(xml)
    self._metatag = None
    
  """
  Should determine immediate xml children, create Xmelements for them, and pass their responsible text. Then those can recursively parse their own xml
  """
  def _parse(self, xml):
    tagstack = []
    for tag in Xmelement._tag_iter(xml):
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
            self._children.append(Xmelement(xml[opentag.end:tag.start]))
      elif tag.type == "selfclose":
        if len(tagstack) == 0:
          self._children.append(Xmelement(xml[tag.start:tag.end]))

    
  @staticmethod
  def _tag_iter(xml):
    for match in re.finditer(r"(</?([^/>]+)>|<([^/>]+)/>)", xml):
      yield XmlTag(match.group(0), match.span())
      
