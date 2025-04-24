
class XmlTag (object):
  def __init__(self, tagstr, span):
    _tagstr = tagstr
    self._attrs = {}
    self._start, self._end = span
    self._type = None
    
    if tagstr.startswith("<?") and tagstr.endswith("?>"):
      self._type = "meta"
      _tagstr = tagstr[2:-2].strip()
    elif tagstr.endswith("/>"):
      self._type = "selfclose"
      _tagstr = tagstr[1:-2].strip()
    elif tagstr.startswith("</"):
      self._type = "close"
      _tagstr = tagstr[2:-1].strip()
    else:
      self._type = "open"
      _tagstr = tagstr[1:-1].strip()

    tagstr_parts = _tagstr.split(" ")
    self._tag = tagstr_parts[0]
    if len(tagstr_parts) > 1:
      for attr in tagstr_parts[1:]:
        attr_parts = attr.split("=")
        if len(attr_parts) == 2:
          self._attrs[attr_parts[0]] = attr_parts[1].strip('"')

  @property
  def start(self):
    return self._start
  
  @property
  def end(self):
    return self._end
  
  @property
  def tag(self):
    return self._tag
  
  @property
  def type(self):
    return self._type
  
  def get_attr(self, attr):
    return self._attrs.get(attr, None)
  
  def has_attr(self, attr):
    return attr in self._attrs
  
  def attr_list(self):
    return self._attrs.keys()
  
  def __repr__(self):
    if self._type == "open":
      return f'<{self.tag}>'
    elif self._type == "close":
      return f'</{self.tag}>'
    elif self._type == "selfclose":
      return f'<{self.tag}/>'
    elif self._type == "meta":
      return f'<?{self.tag}?>'