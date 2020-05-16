#----------------------------Tuples--------------------------------------#

def Create_Tuple(x):
    
    UserTuple = []
    
    for i in range(x):
        
        UserTupleInput = input("Enter the Tuple Value:")
        UserTuple.append(UserTupleInput)
        UserTuple1 = tuple(UserTuple)
    print("Created Tuple values:",UserTuple1)
    return UserTuple1
#count()	Returns the number of times a specified value occurs in a tuple

def count(x):
    val = input("enter the value to count:")
    User_count = x.count(val)
    print("Count of the given value:",User_count)
    return User_count

#index()	Searches the tuple for a specified value and returns the position of where it was found

def index(x):
    val = input("enter the value to check index:\n")
    User_index = x.index(val)
    print("Index postion of given input:",User_index)
    return User_index
#length

def length(x):
    Len = len(x)
    return Len

#slicing

def slicing(x):
    val = int(input("enter the start postion:"))
    val1 = int(input("enter the End postion:"))
    return x[val:val1]
