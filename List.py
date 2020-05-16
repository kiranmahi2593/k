def Create_list(ListInput):
    UserList = []
    for i in range(ListInput):
        UserListInput = input("Enter the List Value:")
        UserList.append(UserListInput)
    print("Created List values:",UserList)
    return UserList

#append()	Adds an element at the end of the list

def append(x):
    val = input("enter the value to append:")
    x.append(val)
    print("List After appending the values:",x)
    return x
    

#length

def length(x):
    Len = len(x)
    return Len
#min

def minimum(x):
    Min = min(x)
    return Min
#Max

def maximum(x):
    Max = max(x)
    return Max

#count()	Returns the number of elements with the specified value

def count(x):
    val = input("enter the value to count:")
    User_count = x.count(val)
    print("Count of the given value:",User_count)
    return User_count

#insert()	Adds an element at the specified position

def insert(x):
    val = int(input("enter the position to insert:"))
    val1 = input("enter the value to insert:")
    x.insert(val,val1)
    print("List After inserting the values:",x)
    return x
# reverse()	Reverses the order of the list

def reverse(x):
    x.reverse()
    print("List After reversing the values:",x)
    return x

#sort()	Sorts the list

def sort(x):
    x.sort()
    print("List After sorting the values:",x)
    return x

#remove()	Removes the first item with the specified value

def remove(x):
    val = input("enter the value to remove:")
    x.remove(val)
    print("List After removing the values:",x)
    return x

#pop()	Removes the element at the specified position

def pop(x):
    val = int(input("enter the position to remove element:"))
    x.pop(val)
    print("List After removing element:",x)
    return x

# copy()	Returns a copy of the list

def copy(x):
    Copy = x.copy()
    print("List of copied values:",Copy)
    return Copy

#clear()	Removes all the elements from the list

def clear(x):
    x.clear()
    print("List After clearing the values:",x)
    return x

# The del keyword can also delete the list completely:

def delete(x):
    del x
    print("List deleted completly")
    return x



    
    

'''    
User_List_Input = Create_list(5)

append(User_List_Input)
'''


   



    
