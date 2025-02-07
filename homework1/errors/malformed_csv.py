
class MalformedCSVException (Exception):
  def __init__(self, msg):
    super().__init__(msg)


class BadCSVRowException (Exception):
  def __init__(self, msg):
    super().__init__(msg)

