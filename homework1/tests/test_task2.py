
import __init__
import task2
import pytest


def test_integer_division():
  assert task2.integer_division(10, 3) == 3


def test_integer_mod():
  assert task2.integer_mod(10, 3) == 1


def test_float_add():
  # known precision issue with floats
  # actual answer: 0.1 + 0.2 = 0.30000000000000004
  assert task2.float_add(0.1, 0.2) != 0.3  
  # we can use rounding to account for precision error
  assert round(task2.float_add(0.1, 0.2), 10) == 0.3
  

def test_do_exponent():
  assert task2.do_exponent(2, 3) == 8  # 2^3 = 8
  assert task2.do_exponent(4, 0) == 1  # 4^0 = 1
  assert task2.do_exponent(16, 0.5) == 4  # sqrt(16) = 4


def test_reverse_string():
  assert task2.reverse_string("hello") == "olleh"
  assert task2.reverse_string("Oh, hi, Mark!") == "!kraM ,ih ,hO"
  assert task2.reverse_string("tacocat") == "tacocat"
  assert task2.reverse_string("imalasagnahog") == "gohangasalami"


def test_concat_strings():
  assert task2.concat_strings("taco", "cat") == "tacocat"
  assert task2.concat_strings("Hi, ", "Mark") == "Hi, Mark"


def test_boolean_and():
  assert task2.boolean_and(True, True) == True
  assert task2.boolean_and(True, False) == False
  assert task2.boolean_and(False, True) == False
  assert task2.boolean_and(False, False) == False


def test_boolean_or():
  assert task2.boolean_or(True, True) == True
  assert task2.boolean_or(True, False) == True
  assert task2.boolean_or(False, True) == True
  assert task2.boolean_or(False, False) == False


def test_boolean_xor():
  assert task2.boolean_xor(False, False) == False
  assert task2.boolean_xor(True, False) == True
  assert task2.boolean_xor(False, True) == True
  assert task2.boolean_xor(True, True) == False


pass
