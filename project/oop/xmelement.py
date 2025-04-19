
import re


class Xmelement (object):
  def __init__(self, xml, is_root=False):
    self._is_root = is_root
    self._children = []
    self._properties = {}
    self._inner_text = ""
    self._parse(xml)
    
  """
  Should determine immediate xml children, create Xmelements for them, and pass their responsible text. Then those can recursively parse their own xml
  """
  def _parse(self, xml):
    for tag in Xmelement._tag_iter(xml):
      print(tag)
    
  @staticmethod
  def _tag_iter(xml):
    for match in re.finditer(r"(</?([^/>])+>|<([^/>])+/>)"):
      print(match)

