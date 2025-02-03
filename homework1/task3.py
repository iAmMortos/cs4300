
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


"""
An implementation of the sieve of Eratosthenes that runs
up to N primes instead of finding every prime under N.
Theoretically inifinite, but the shifting list of Booleans 
will obviously, eventually run out of memory.
"""
def print_first_n_primes(n_primes, print_all=True):
  if type(n_primes) is not int or n_primes <= 0:
    raise Exception("Invalid number n_primes. Must be positive integer.")
  primes = [2, 3]  # first two primes
  ce = primes[-1]  # "old ceiling" initialized so while loop can operate smoothly
  # Sift numbers and find primes until we've reached our "prime quota" n_primes.
  while len(primes) < n_primes:
    # Shift our sieve up by moving the floor and ceiling
    fl = ce + 1  # floor of the sieve (the previous ceiling + 1)
    ce = fl * 2  # ceiling of the sieve (the current floor x 2)
    # Based on Bertrand's postulate, that says for every number n > 3,
    #   there exists a prime p s.t. n < p < 2n. So our floor and ceiling
    #   will act as our n and 2n
    # Initialize our "sieve" to "Trues".
    nums = [True for _ in range(fl, ce + 1)]
    for p in primes:
      # "sift" the numbers in the sieve range, setting all multiples of previous
      #   primes to False.
      # Find the first multiple of prime p that falls within the range of the sieve
      first = ((fl // p) + (0 if fl % p == 0 else 1)) * p
      for n in range(first, ce+1, p):
        nums[n - fl] = False  # n is not a prime; it's a multiple of another prime
        
    # Any "Trues" left in the sieve represent prime numbers.
    # Add each to our primes list
    i = 0  # starting index for searching for Trues in our list
    for _ in range(nums.count(True)):
      p = nums.index(True, i)
      i = p + 1
      primes.append(p + fl)
    
  # printing takes a lot of processing, but calculation is pretty fast!
  if print_all:
    print('\n'.join([str(p) for p in primes[:n_primes]]))
  else:
    # just print the Nth prime. Much faster
    print(primes[n_primes-1])
  

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
  print(f"Slow summing 100,000,000 numbers took {round((end - start) * 1000, 3)} millis.")
  
  start = timer()
  print(sum_first_n_numbers_fast(100_000_000))
  end = timer()
  print(f"Fast summing 100,000,000 numbers took {round((end - start) * 1000, 3)} millis.")
  
  start = timer()
  print(sum_first_n_numbers_fast(1_234_567_890_123_456_789))
  end = timer()
  print(f"Fast summing 1,234,567,890,123,456,789 numbers took {round((end - start) * 1000, 3)} millis.")
  
  N = 100
  s = timer()
  print_first_n_primes(N, print_all=False)
  print(f"{N}th prime found in {round((timer() - s) * 1000, 3)} millis")
