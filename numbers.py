

###########Function to add the values#################

def sum(x,y):
    z = x + y
    return z

##########Function to subtract the values#############

def sub(x,y):
    z = x - y
    return z

#########Function to multiply the values##############

def mul(x,y):
    z = x * y
    return z

#########Function to divide the values################


def div(x,y):
    z = x / y
    return z
        

#########Function to floor division the values#########

def floor(x,y):
    z = x // y
    return z
        
  
#########Function to power the values#################

def power(x):
    z = x ** 2
    return z
#########Function to modulus the values#################

def mod(x,y):
    z = x % y
    return z



#########Function to square the values#################

def square(x):
    z = x * x
    return z

#########Function to squareroot the values#################

def squrt(x):
    z = x ** 0.5
    return z

#########Function to cube the values#################

def cube(x):
    return x * x * x

#########Function to cube root the values#################

def cube_root(x):
    return x **(1/3)


#########Function to check prime number #################

def prime(x):
    
    if x > 1:
        
        for i in range(2,x):
            
           if (x % i) == 0:
               print(x,"is not a prime number")
               
               break
        else:
            
           print(x,"is a prime number")
       
    else:
        
        print(x,"is not a prime number")
    
   
    
#########Function to check armstrong number #################
def armstrong(number):

 
    sum = 0
 
    temp = number
    while temp > 0:
       digit = temp % 10
       sum += digit ** 3
       temp //= 10
    if number == sum:
        print(number, "is an Armstrong number")
    else:
            print(number, "is not an Armstrong number")
        
        
        
#########Function to check fibonosis series #################
def Fibonacci(num):
    initial = 0
    current = 1
    for i in range(num):
        sum1 = initial + current
        print(sum1)
        initial = current
        current = sum1

#########Function to check factorial #################

def factorial(x):
    if x == 0:
        return 1
    else:
        return x * factorial(x-1)


#########Function to check odd or even #################

def odd_even(x):
    if x % 2 == 0:
        print("The Number is even")
    else:
            print("The Number is ODD")


#########Function to check positive and negative #################

def Postive_Negative(x):
    if x > 0:
        print("The Number is positive")
    else:
            print("The Number is Negative")
