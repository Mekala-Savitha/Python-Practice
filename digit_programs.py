# Digit-Based Programs in Python
# Author-Savitha

# Count Digits 
def count_digits(n):
  count=0
  while n>0:
    count+=1
    n=n//10
  return count
print(count_digits(7529))

# Sum of Digits
def sum_digits(n):
    total = 0
    while n > 0:
        digit = n % 10
        total = total + digit
        n = n // 10
    return total
print(sum_digits(7823))

# Product of Digits 
def product_of_digits(n):
  product=1
  while n>0:
    digit=n%10
    product=product*digit
  return product 
print(product_of_digits(1234))

# Reverse a Number
def rev_number(n):
  rev=0
  while n>0:
    digit=n%10
    rev=rev*10+digit
    n=n//10
  return rev
print(rev_number(8765))

# Palindrome Number
def palindrome(n):
  temp=n
  rev=0
  while n>0:
    digit=n%10
    rev=rev*10+digit 
    n=n//10
  if temp==rev:
    print("Palindrome")
  else:
    print("Not Palindrome")
palindrome(121)

# Armstrong Number 
def armstrong(n):
  temp=n
  total=0
  while n>0:
    digit=n%10
    total=total+digit**3
    n=n//10
  if total==temp:
    print("Armstrong")
  else:
    print("Not Armstrong")
armstrong(153)

# Largest Digit 
def largest_digit(n):
  largest=0
  while n>0:
      digit=n%10
      if digit>largest:
          largest=digit
      n=n//10
  return largest
print(largest_digit(58392))

# Smallest Digit 
def smallest_digit(n):
  smallest=9
  while n>0:
    digit=n%10
    if digit<smallest:
      smallest=digit
    n=n//10
  return smallest 
print(smallest_digit(42891))

# Count Even Digits
def count_even_digits(n):
  count=0
  while n>0:
    digit=n%10
    if digit%2==0:
      count+=1
    n=n//10
  return count
print(count_even_digits(24691))

# Count Odd Digits
def count_odd_digits(n):
  count=0
  while n>0:
    digit=n%10
    if digit%2==1:
      count+=1
    n=n//10
  return count 
print(count_odd_digits(14782))

# Count Zero Digits
def count_zero_digits(n):
  count=0
  while n>0:
    digit=n%10
    if digits==0:
      count+=1
    n=n//10
  return count
print(count_zero_digits(1002060))

# Count of Non Zero Digits
def count_non_zero_digits(n):
    count = 0
    while n > 0:
        digit = n % 10
        if digit != 0:
            count += 1
        n = n // 10
    return count
print(count_non_zero_digits(1520053))

# Count Occurances of 5
def digit(n):
  count=0
  while n>0:
    digit=n%10
    if digit==5:
      count+=1
    n=n//10
  return count
print(digit(155895595))

# First Digit of a Number 
def first_digit(n):
  while n>=10:
    digit=n%10
    n=n//10
  return n
print(first_digit(1826))

# Last Digit of a Number 
def last_digit(n):
  return n%10
print(last_digit(3278))

# Sum of Even Digits
def sum_even_digits(n):
  total=0
  while n>0:
    digit=n%10
    if digit%2==0:
      total=total+digit
    n=n//10
  return total
print(sum_even_digits(123456))

# Sum of Odd Digits
def sum_odd_digits(n):
  total=0
  while n>0:
    digit=n%10
    if digit%2==1:
      total=total+digit
    n=n//10
  return total
print(sum_odd_digits(123456))

# Largest Even Digit 
def largest_even_digit(n):
  largest=0
  while n>0:
    digit=n%10
    if digit%2==0:
      if digit>largest:
        largest=digit
    n=n//10
  return largest
print(largest_even_digit(5839264))

# Product of Even Digits
def product_of_even_digits(n):
  produt=1
  while n>0:
    digit=n%10
    if digit%2==0:
      product=product*digit 
    n=n//10
  return product 
print(produt_of_even_digits(123456))

# Product of Odd Digits
def product_of_odd_digits(n):
  product=1
  while n>0:
    digit=n%10
    if digit%2==1:
      produt=product*digit
    n=n//10
  return product 
print(product_of_odd_digits(123456))
  
