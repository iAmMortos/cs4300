
import __init__
import task2
import pytest


def test_add_integers():
  val = task2.add_integers(2, 5)
  assert type(val) is int
  assert val == 7
  assert task2.add_integers(1.0, 2.5) == 3.5
  
  with pytest.raises(Exception) as exc_info:
    raise Exception('some info')
  assert exc_info.value.args[0] == 'some info'
  assert str(exc_info.value) == 'some info'
