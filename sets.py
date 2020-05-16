#------------------------Set--------------------------------#

def Create_Set(SetInput):
    UserSet = set()
    for i in range(SetInput):
        UserSetInput = input("Enter the set Value:")
        UserSet.add(UserSetInput)
    print("Created Set:",UserSet)
    return UserSet

#add()	Adds an element at the end of the list

def AddSet(x):
    val = input("enter the value to Add:")
    x.add(val)
    print("Set After Adding the values:",x)
    return x
    
#clear()	Removes all the elements from the set

def clear(x):
    x.clear()
    print("Set After clearing the values:",x)
    return x

#copy()	Returns a copy of the set

def copy(x):
    Copy = x.copy()
    print("Set of copied values:",Copy)
    return Copy
#difference()	Returns a set containing the difference between two or more sets

def difference(x):
    z = x.difference(y)
    return z

# difference_update()	Removes the items in this set that are also included in another, specified set

def difference_update(x):
    x.difference_update(y)
    return x

#discard()	Remove the specified item

def discard(x):
        
    x.discard(val)
    print("Set After discarding the element:",x)
    return x


# intersection()	Returns a set, that is the intersection of two other sets

def intersection(x):
    z = x.intersection(y)
    return z

# intersection_update()	Removes the items in this set that are not present in other, specified set(s)
    
def intersection_update(x):
    x.intersection_update(y)
    return x
#pop()		Removes an element from the set

def pop(x):
    x.pop()
    print("Set afer pop:",x)
    return x

#remove()	Removes the first item with the specified value

def remove(x):
    val = input("enter the value to remove:")
    x.remove(val)
    print("Set After removing the values:",x)
    return x
#symmetric_difference()	Returns a set with the symmetric differences of two sets

def symmetric_difference(x):
    z = x.symmetric_difference(y)
    return z

#symmetric_difference_update()	inserts the symmetric differences from this set and another

def symmetric_difference_update(x):
    x.symmetric_difference_update(y)
    return x

#union()	Return a set containing the union of sets

def union(x):
    z = x.union(y)
    return z

# update()	Update the set with the union of this set and others

def update(x):
    x.update(y)
    return x
