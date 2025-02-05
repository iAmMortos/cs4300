
"""
If the discount_percent_off is given as a value less than or equal to 1, 
it'll be treated as a percentage already and be directly applied.

If the discount_percent_off is given as a value over 1, it'll be treated
as a value that needs to be divided by 100 first.

This function assumes a discound less than 1% will ever be required.
"""
def calculate_discount(price, discount_percent_off):
  if 0 <= discount_percent_off <= 1:
    return price * (1 - discount_percent_off)
  elif 1 < discount_percent_off <= 100:
    return price * (1 - (discount_percent_off / 100))
  else:
    raise Exception("Invalid discount value given. Must be in range [0, 100]")
    

def price_as_string(price):
  return f"${price:.2f}"


if __name__ == '__main__':
  print(price_as_string(calculate_discount(20.00, 20)))
  print(price_as_string(calculate_discount(20.00, 0.2)))
  print(price_as_string(calculate_discount(30, 33.33)))
  print(price_as_string(calculate_discount(30, 1/3)))
  print(price_as_string(calculate_discount(50, 33.33)))
  print(price_as_string(calculate_discount(50, 1/3)))
  print(price_as_string(calculate_discount(100, 0)))
  print(price_as_string(calculate_discount(5, 100)))

