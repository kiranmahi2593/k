#--------------------------Dictionaries-------------------------------------#
def Create_dict(DictInput):
    Userdict = dict()
    for i in range(DictInput):
        UserDictKey = input("Enter the Key:")
        UserDictValue = input("Enter the Value:")
        
        Userdict[UserDictKey] = UserDictValue
    print("Created Dictionaty",Userdict)
    return Userdict

#clear()	Removes all the elements from the dictionary

def clear(x):
    x.clear()
    print("Dictionary After clearing the values:",x)
    return x

#copy()	Returns a copy of the dictionary

def copy(x):
    Copy = x.copy()
    print("Dict of copied values:",Copy)
    return Copy
#fromkeys()	Returns a dictionary with the specified keys and value

def fromkeys(x):
    thisdict = dict.fromkeys(x)
    return thisdict

#get()	Returns the value of the specified key
'''
def get(x):
    val = int(input("enter the key:"))
    y = x.get(val)
    print("Output:",y)
    return y
'''
#items()	Returns a list containing a tuple for each key value pair

def items(x):
    items_user = x.items()
    print("Output:",items_user)
    return items_user
#keys()	Returns a list containing the dictionary's keys
def keys(x):
    items_keys = x.keys()
    print("Output:",items_keys)
    return items_keys
#pop()	Removes the element with the specified key

def pop(x):
    val = input("enter the key name to remove dict:")
    x.pop(val)
    print("Dict After removing dict:",x)
    return x
#popitem()	Removes the last inserted key-value pair

def popitem(x):
    x.popitem()
    print("Dict After removing popitem:",x)
    return x
#setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value

def setdefault(x):
    UserDictKey = input("Enter the Key:")    
    UserDictValue = input("Enter the Value:")
    SetFunction = x.setdefault(UserDictKey,UserDictValue)
    print("OutPut",SetFunction)
    return SetFunction
#update()	Updates the dictionary with the specified key-value pairs

def update(x):
    UserDictKey = input("Enter the Key:")    
    UserDictValue = input("Enter the Value:")
    UpdateFunction = x.update(UserDictKey,UserDictValue)
    print("OutPut",UpdateFunction)
    return UpdateFunction
#values()	Returns a list of all the values in the dictionary
def values(x):
    items_values = x.values()
    print("Output:",items_values)
    return items_values
