# Assingment 1.1: WAP to print your name three times
# Assingment 2.1: WAP to add three numbers and print the result.
# Assingment 2.2: WAP to concatinate three strings and print the result.
# Assingment 4.1: WAP to print the table of 7, 9.
# Assingment 4.2: WAP to print the table of n and n is given by user.
# Assingment 4.3: WAP to add all the numbers from 1 to n and n is given by user.
# Assingment 5.1: WAP to find max amoung three numbers and input from user. [Try max() function]
# Assingment 5.2: WAP to add all numbers divisible by 7 and 9 from 1 to n and n is given by the user.
# Assingment 5.3: WAP to add all prime numbers from 1 to n and n is given by the user.
# Assingment 6.1: WAP using function that add all odd numbers from 1 to n, n is given by the user.
# Assingment 6.2: WAP using function that add all prime numbers from 1 to n, n given by the user


# 1.2
def print_name():
    name = "Rohit"
    print(name * 3)

# 2.1
def add_three_numbers():
    a = 10
    b = 20
    c = 30
    print(a + b + c)
    
# 2.2
def concat_three_strings():
    a = "Hello "
    b = "World "
    c = "Python"
    print(a + b + c)

# 4.1
def table_of_n(n):
    for i in range(1, 11):
        print(n * i)
        
# 4,2
def add_all_numbers(n):
    total = 0
    for i in range(1, n+1):
        total += i
    print(total)

# 4.3
def max_amoung_three_numbers(a, b, c):
    print(max(a, b, c))
    
# 5.1
def add_divisible_by_7_and_9(n):
    total = 0
    for i in range(1, n+1):
        if i % 7 == 0 and i % 9 == 0:
            total += i
    print(total)

# 5.2
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

# 5.3
def add_prime_numbers(n):
    total = 0
    for i in range(1, n+1):
        if is_prime(i):
            total += i
    print(total)
    
# 6.1
def add_odd_numbers(n):
    total = 0
    for i in range(1, n+1):
        if i % 2 != 0:
            total += i
    print(total)

# 6.2
def add_prime_numbers(n):
    total = 0
    for i in range(1, n+1):
        if is_prime(i):
            total += i
    print(total)

if __name__ == "__main__":
    print_name()
    add_three_numbers()
    concat_three_strings()
    table_of_n(7)
    table_of_n(9)
    add_all_numbers(10)
    max_amoung_three_numbers(10, 20, 30)
    add_divisible_by_7_and_9(100)
    add_prime_numbers(100)
    add_odd_numbers(100)
    add_prime_numbers(100)
    