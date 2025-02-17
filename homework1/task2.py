
from numbers import Number


def integer_division(a:int, b:int):
  """
  perform integer division: a // b
  e.g. 5/2 = 2
  """
  return a // b


def integer_mod(a:int, b:int):
  """a mod b"""
  return a % b


def float_add(a:float, b:float):
  """add two floats"""
  return a + b


def do_exponent(base, exponent):
  """Perform exponentiation: base ^ exponent"""
  return base ** exponent


def reverse_string(s:str):
  """Reverse the given string"""
  return s[::-1]


def concat_strings(a:str, b:str):
  """Concatenate two strings"""
  return a + b


def boolean_and(a:bool, b:bool) -> bool:
  """Perform a bitwise AND on the two boolean values"""
  return a and b


def boolean_or(a:bool, b:bool) -> bool:
  """Performs a bitwise OR on the two boolean values"""
  return a or b


def boolean_xor(a:bool, b:bool) -> bool:
  """Performs a bitwise XOR on the two boolean values"""
  return a ^ b
