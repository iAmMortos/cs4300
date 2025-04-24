class TextNode(object):
  def __init__(self, text):
    self._value = text
  @property
  def value(self):
    return self._value