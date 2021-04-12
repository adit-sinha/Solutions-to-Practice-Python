n = int(input("Give me a number greater than 1: "))
x = range(2,n)
divisors = [a for a in x if n % a == 0]
if divisors == [] and n>1:
 print("{} is a prime number.".format(n))
elif n<=1:
 print("Please give a number greater than 1.".format(n))
else:
 print("{} is composite number whose divisors are {}.".format(n,divisors))
