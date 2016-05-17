#Project Euler #1

#Prompt:
#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.

#sigma sums the numbers from 1 to end (inclusive)
def sigma(end):
  #Sum identity
  return (end * (end + 1) / 2)

sum3 = 3 * sigma(333)
sum5 = 5 * sigma(199)
sum15 = 15 * sigma(66)

print sum3 + sum5 - sum15
