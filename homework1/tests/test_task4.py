import context
import task4


def test_calculate_discount():
  assert task4.calculate_discount(20.00, 20)           == 16
  assert task4.calculate_discount(20.00, 0.2)          == 16
  assert task4.calculate_discount(30, 33.33)           == 20.001
  # We round these values to account for floating point error
  assert round(task4.calculate_discount(30, 1/3), 10)  == 20
  assert round(task4.calculate_discount(50, 33.33), 2) == 33.34
  assert round(task4.calculate_discount(50, 1/3), 5)   == 33.33333
  assert task4.calculate_discount(100, 0)              == 100
  assert task4.calculate_discount(5, 100)              == 0

def test_price_as_string():
  assert task4.price_as_string(0.05)     == "$0.05"
  assert task4.price_as_string(0.005)    == "$0.01"
  assert task4.price_as_string(16)       == "$16.00"
  assert task4.price_as_string(20.001)   == "$20.00"
  assert task4.price_as_string(20)       == "$20.00"
  assert task4.price_as_string(33.34)    == "$33.34"
  assert task4.price_as_string(33.33333) == "$33.33"
  assert task4.price_as_string(66.66666) == "$66.67"
  assert task4.price_as_string(100)      == "$100.00"
  assert task4.price_as_string(0)        == "$0.00"
  assert task4.price_as_string(19.999)   == "$20.00"
  
