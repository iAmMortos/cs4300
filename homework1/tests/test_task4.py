import __init__
import task4


def test_calculate_discount():
  assert task4.calculate_discount(20.00, 20) == 16
  assert task4.calculate_discount(20.00, 0.2) == 16
  assert task4.calculate_discount(30, 33.33) == 20
  assert task4.calculate_discount(30, 1/3) == 20
  assert task4.calculate_discount(50, 33.33) == 33.33
  assert task4.calculate_discount(50, 1/3) == 33.33
  assert task4.calculate_discount(100, 0) == 100
  assert task4.calculate_discount(5, 100) == 0

