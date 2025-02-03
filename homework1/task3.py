
from timeit import default_timer as timer

"""
Tests the sign of the given number.
Returns:
  1 if it's positive
  -1 if it's negative
  0 if it's zero
"""
def test_polarity(n):
  if n > 0:
    return 1
  elif n < 0:
    return -1
  else:
    return 0


def print_first_n_primes(n):
  primes = []
  nums = []
  # 0 and 1 are not prime
  n = 2
  

def sum_first_n_numbers(n):
  # iterate numbers 1 - n, and keep a running sum
  c = 0
  for i in range(1, n+1):
    c += i
  return c
  

def sum_first_n_numbers_fast(n):
  # no loop, just some arithmetic
  t = 0
  # determine if given number is odd
  if n % 2 == 1:
    # if it is, add that extra odd number to our total
    #   then use the next even number down for everything else.
    maxn = n - 1
    t = n
  else:
    maxn = n
  # maxn will be even by this point.
  # multiply half of maxn by (maxn + 1). Equivalent to sum of numbers
  return t + (maxn // 2) * (maxn + 1)
  

if __name__ == '__main__':
  start = timer()
  print(sum_first_n_numbers(100_000_000))
  end = timer()
  print(f"Slow summing 100,000,000 numbers took {round(end - start, 3)} seconds.")
  
  start = timer()
  print(sum_first_n_numbers_fast(100_000_000))
  end = timer()
  print(f"Fast summing 100,000,000 numbers took {round(end - start, 3)} seconds.")
  
  start = timer()
  print(sum_first_n_numbers_fast(1_234_567_890_123_456_789))
  end = timer()
  print(f"Fast summing 1,234,567,890,123,456,789 numbers took {round(end - start, 3)} seconds.")

