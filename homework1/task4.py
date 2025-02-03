
"""
If the discount_percent_off is given as a value less than or equal to 1, 
it'll be treated as a percentage already and be directly applied.

If the discount_percent_off is given as a value over 1, it'll be treated
as a value that needs to be divided by 100 first.
"""
def calculate_discount(price, discount_percent_off):
  if 0 <= discount_percent_off <= 1:
    pass
  elif 1 < discount_percent_off <= 100:
    pass
  else:
    pass
  


if __name__ == '__main__':
  pass
