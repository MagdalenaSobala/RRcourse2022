### HOMEWORK 21.04.2022 ###

##EX.1
#Consider a FizzBuzz problem. The program should write numbers from 1 to 100, 
#separated by a newline, but multiples of 3 and of 5 should be replaced with 
#“Fizz” and “Buzz” respectively. For numbers which are multiples of both 3 and 5 
#print “FizzBuzz”. Write a readable and working solution in your preferred language.

for i in range(101): #we want the 100 to be included
    if i%3==0: #divisble by 3
        if i%5==0: #divisble by 3 and divisible by 5
            print('FizzBuzz')
        else: #divisble by 3 but no by 5
            print('Fizz')
    elif i%5==0: #divisble by 5
        if i%3==0: #divisble by 5 and divisible by 3
            print('FizzBuzz')
        else: #divisble by 5 but no by 3
            print('Buzz')
    else: #not divisible by either 3 nor 5
        print(i)


##EX.2
##part1
#Write a function which takes n (float or integer) as a parameter and returns the largest 
#Fibonacci number smaller than n. The function should be documented, with type hints, and 
#appropriate comments. 

def largest_fib(n: float) -> float:
    """Returns the largest Fibonnaci number smaller than provided parameter"""
    a1=0 #first number in the Fib. sequence
    a2=1 #second number in the Fib. sequence
    while a1+a2<n: #loops through the Fib. sequence as long as the last two numbers are smaller than n
        a1=a1+a2 #Fib. sequence condition
        a2,a1=a1,a2 #change the places of the numbers in the sequence
    return max(a1,a2) #required to check the while loop condition

##part2
#Write a function which reverses digits in an integer number (for example 7245 -> 5427). 
#The function should be documented, with type hints, and appropriate comments.

def reverse_int_digits(number: int) -> int: #in case of syntax error make sure your python version is up to date
    """Returns integer number w/inverse order of digits"""
    return int(str(number)[::-1]) #rearranges the order of the elements of a string and converts back to integer