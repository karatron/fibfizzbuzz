#!/usr/bin/pypy
#generates the first n Fibonacci numbers F(n), printing
# "Buzz" when F(n) is divisible by 3.
# "Fizz" when F(n) is divisible by 5.
# "BuzzFizz" when F(n) is prime.
# the value F(n) otherwise.

import numpy
import argparse

def __main__():
  parser = argparse.ArgumentParser(description='Fibonacci Fiz Buzz.')
  parser.add_argument('nums', type = int, nargs=1, help = 'number of Fibonacci numbers.  Must be in the range 1-92')

  args = parser.parse_args()

  #Greater than 92 causes overflow.  No requirement for max....
  nums = args.nums[0]
  if nums < 1 or nums > 92:
    parser.print_help()
    exit()

  #The Fibonacci Matrix
  fib_matrix = numpy.matrix([[1, 1], [1, 0]])

  for n in xrange(nums):
    fib_num = (fib_matrix**n)[0,0]

    if fib_num % 3 == 0:
      if fib_num == 3:
        print "Buzz, BuzzFizz"
      else:
        print "Buzz"

    elif fib_num % 5 == 0:
      if fib_num == 5:
        print "Fizz, BuzzFizz"
      else:
        print "Fizz"

    elif is_prime(fib_num):
      print "BuzzFizz"

    else:
      print fib_num

def is_prime(num):
  #The cool check starts at 3...
  if num == 1:
    return False
  elif num == 2:
    return True

  # Fermat can say not prime
  elif (2 << (num - 2)) % num != 1:
    return False

  # Otherwise, brute force.,,
  else:
    for den in xrange(2, (num/2-1)):
      if num%den == 0:
        return False

    return True





__main__()