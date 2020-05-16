#capitalize()	Converts the first character to upper case

def capitalize(name):    
    CName = name.capitalize()
    return CName
    
#casefold()	Converts string into lower case

def casefold(name):    
    CName = name.casefold()
    return CName

#center()	Returns a centered string

def center(name,y):
    CName = name.center(y)
    return CName
#count()	Returns the number of times a specified value occurs in a string

def count(name,y):
    CName = name.count(y)
    return CName

#encode()	Returns an encoded version of the string
  

def encode(name):
    CName = name.encode()
    return CName

#endswith()	Returns true if the string ends with the specified value

def endswith(name,y):
    CName = name.endswith(y)
    return CName
#expandtabs()	Sets the tab size of the string

def expandtabs(name,y):
    CName = name.expandtabs(y)
    return CName
#find()	Searches the string for a specified value and returns the position of where it was found

def find(name,y):
    CName = name.find(y)
    return CName
#format()	Formats specified values in a string

def format(name,y):
    CName = name.format(y)
    return CName

#index()	Searches the string for a specified value and returns the position of where it was found

def index(name,y):
    CName = name.index(y)
    return CName

#isalnum()	Returns True if all characters in the string are alphanumeric


def isalnum(name):
    CName = name.isalnum()
    return CName

#isalpha()	Returns True if all characters in the string are in the alphabet

def isalpha(name):
    CName = name.isalpha()
    return CName

#isdecimal()	Returns True if all characters in the string are decimals

def isdecimal(name):
    CName = name.isdecimal()
    return CName

#isdigit()	Returns True if all characters in the string are digits

def isdigit(name):
    CName = name.isdigit()
    return CName

#isidentifier()	Returns True if the string is an identifier (A string is considered a valid identifier if it only contains alphanumeric letters (a-z) and (0-9), or underscores (_). A valid identifier cannot start with a number, or contain any spaces.)


def isidentifier(name):
    CName = name.isidentifier()
    return CName

#islower()	Returns True if all characters in the string are lower case (Numbers, symbols and spaces are not checked, only alphabet characters.)


def islower(name):
    CName = name.islower()
    return CName

#The isnumeric() method returns True if all the characters are numeric (0-9), otherwise False.Exponents, like ² and ¾ are also considered to be numeric values.

def isnumeric(name):
    CName = name.isnumeric()
    return CName

#isprintable()	Returns True if all characters in the string are printable(Example of none printable character can be carriage return and line feed.)

def isprintable(name):
    CName = name.isprintable()
    return CName

#The isspace() method returns True if all the characters in a string are whitespaces, otherwise False.

def isspace(name):
    CName = name.isspace()
    return CName
#The istitle() method returns True if all words in a text start with a upper case letter, AND the rest of the word are lower case letters, otherwise False.Symbols and numbers are ignored

def istitle(name):
    CName = name.istitle()
    return CName

#The isupper() method returns True if all the characters are in upper case, otherwise False.Numbers, symbols and spaces are not checked, only alphabet characters.

def isupper(name):
    CName = name.isupper()
    return CName

#The join() method takes all items in an iterable and joins them into one string.A string must be specified as the separator.

def join():
    names = input("enter the string :")
    delimiter = input("enter the delimitter i.e ',' :")
    single_str = delimiter.join(names)
    print('String: {0}'.format(single_str))
    return single_str

#ljust()	Returns a left justified version of the string

def ljust(name,y):
    CName = name.ljust(y)
    return CName
#lower()	Converts a string into lower case

def lower(name):
    CName = name.lower()
    return CName

#The lstrip() method removes any leading characters (space is the default leading character to remove)

def lstrip(name):
    CName = name.lstrip()
    return CName

#partition() (Returns a tuple where the string is parted into three parts)


def partition(name,y):
    CName = name.partition(y)
    return CName

# The replace() method replaces a specified phrase with another specified phrase.

def replace():
    String_Input = input("enter the string to check replace function:")
    String_Input1 = input("enter the string to be replace:")
    String_Input2 = input("enter the new string to be added:")
    x = String_Input.replace(String_Input1,String_Input2)
    print("Output:",x)

#rfind()	Searches the string for a specified value and returns the last position of where it was found

def rfind(name,y):
    CName = name.rfind(y)
    return CName

#rindex()	Searches the string for a specified value and returns the last position of where it was found

def rindex(name,y):
    CName = name.rindex(y)
    return CName
#The rjust() method will right align the string, using a specified character (space is default) as the fill character.

def rjust(name,y):
    CName = name.rjust(y)
    return CName

#The rpartition() method searches for the last occurrence of a specified string, and splits the string into a tuple containing three elements.

def rpartition(name,y):
    CName = name.rpartition(y)
    return CName

#The rsplit() method splits a string into a list, starting from the right.If no "max" is specified, this method will return the same as the split() method.


def rsplit(name,y):
    CName = name.rsplit(y)
    return CName

#The rstrip() method removes any trailing characters (characters at the end a string), space is the default trailing character to remove.

def rstrip(name,y):
    CName = name.rstrip(y)
    return CName

#The split() method splits a string into a list.You can specify the separator, default separator is any whitespace.

def split(name):
    CName = name.split()
    return CName

#The splitlines() method splits a string into a list. The splitting is done at line breaks.

def splitlines(name):
    CName = name.splitlines()
    return CName

#The startswith() method returns True if the string starts with the specified value, otherwise False.

def startswith(name,y):
    CName = name.startswith(y)
    return CName
#strip() Remove spaces at the beginning and at the end of the string

def strip(name):
    CName = name.strip()
    return CName

#The swapcase() method returns a string where all the upper case letters are lower case and vice versa.


def swapcase(name):
    CName = name.swapcase()
    return CName

#The title() method returns a string where the first character in every word is upper case.
#Like a header, or a title.If the word contains a number or a symbol, the first letter after that will be converted to upper case.

def title(name):
    CName = name.title()
    return CName

#upper()	Converts a string into upper case

def upper(name):
    CName = name.upper()
    return CName

#The zfill() method adds zeros (0) at the beginning of the string,
#until it reaches the specified length.

def zfill(name,y):
    CName = name.zfill(y)
    return CName


#Palindrome

def palindrome(num):
    try:
        
        if str(num) == str(num)[::-1]:
            print('The given number is PALINDROME')
        else:
            print('The given number is NOT a palindrome')
    except ValueError:
        print("That's not a valid number, Try Again !")
            
        
#ADD two strings
def Add_Two_Strings(x,y):
    CN = x + y
    return CN
#length

def length(x):
    CN = len(x)
    return CN
        
    
#ASCII Chnaracter

def ASCII(x):
    print("The ASCII Value = %d" %ord(x[0]))
    return x

#vowels

def vowels(x):
    count = 0
    string = x.lower()
    for char in string:
        if char in 'aeiou':
            count += 1
    print ("The count of vowel in given input:",count)
            
#reverse
    
def reverse(string):
    return string[::-1]
    

        

    
    

 





    
        

  









