
fib_lookup = dict()

def fibonacci(num):

   if num == 1 or num ==0:
      fib_lookup[num]=num
   else:
      if 'num' not in fib_lookup:
         fib_lookup[num] = fibonacci(num-1) + fibonacci(num-2)
   return fib_lookup[num]

print (fibonacci(5))
