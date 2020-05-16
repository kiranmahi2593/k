
print("=============================================")
print("****** Welcome to DS DT Calculator***********")
print("=============================================")

dsdtdict = {"1":"Number","2":"String","3":"List","4":"tuple","5":"Set","6":"Dictionary","7":"Exit"}

while True:
    
    print("The List of Operations can be performed in this Calculator:\n\n",dsdtdict)

    UserChoice = input("\n\nSelect any one number to perform the operation:")

#---------------------------Number Operations----------------------------------------#

    if UserChoice == "1":
    
    
        
        
        Numberdict = {"1":"sum","2":"sub","3":"mul","4":"div","5":"floor","6":"power","7":"mod","8":"square","9":"squrt","10":"cube","11":"cube_root","12":"prime","13":"armstrong","14":"Fibonacci","15":"factorial","16":"odd_even","17":"Postive_Negative","18":"Exit"}    
        while True:
            print('\n\nAvailable functions in numbers:\n\n',Numberdict)
        
            import numbers
            Number_Input = input("\n\nSelect any one number to perform the operation:")
            if Number_Input == "1":
                print("\n\n UserGuide : Sum function used to Add Two Values")
                Sum_Input = int(input("\nEnter the first value:"))
                Sum_Input1 = int(input("Enter the second value:"))
                print("The Sum of Given value :",numbers.sum(Sum_Input,Sum_Input1))
            elif Number_Input == "2":
                print("\n\n UserGuide : Sub function used to subtract Two Values")
                Sub_Input = int(input("\nEnter the first value:"))
                Sub_Input1 = int(input("Enter the second value:"))
                print("The Sub output of Given value :",numbers.sub(Sub_Input,Sub_Input1))
            elif Number_Input == "3":
                print("\n\n UserGuide : mul function used to multiply Two Values")
                Mul_Input = int(input("\nEnter the first value:"))
                Mul_Input1 = int(input("Enter the second value:"))
                print("The mul output of Given value :",numbers.mul(Mul_Input,Mul_Input1))
            elif Number_Input == "4":
                print("\n\n UserGuide : div function used to divide Two Values")
                div_Input = int(input("\nEnter the first value:"))
                div_Input1 = int(input("Enter the second value:"))
                print("The div output of Given value :",numbers.div(div_Input,div_Input1))
            elif Number_Input == "5":
               print("\n\n UserGuide : floor function:Returns the integral part of the quotient")
               Fdiv_Input = int(input("\nEnter the first value:"))
               Fdiv_Input1 = int(input("Enter the second value:"))
               print("The floor output of Given value :",numbers.floor(Fdiv_Input,Fdiv_Input1))
            elif Number_Input == "6":
               print("\n\n UserGuide : power function used to power the value")
               Pow_Input = int(input("\nEnter the value:"))
               print("The power output of Given value :",numbers.power(Pow_Input))
            elif Number_Input == "7":
               print("\n\n UserGuide : mod function:used for remainder division on integers")
               Mdiv_Input = int(input("\nEnter the first value:"))
               Mdiv_Input1 = int(input("Enter the second value:"))
               print("The mod output of Given value :",numbers.mod(Mdiv_Input,Mdiv_Input1))
            elif Number_Input == "8":
               print("\n\n UserGuide : square function:returns the square of any number")
               Sq_Input = int(input("\nEnter the value:"))
               print("The square output of Given value :",numbers.square(Sq_Input))
            elif Number_Input == "9":
               print("\n\n UserGuide : square root function:returns the square root of any number")
               Sqrt_Input = int(input("\nEnter the value:"))
               print("The square root output of Given value :",numbers.squrt(Sqrt_Input))
            elif Number_Input == "10":
               print("\n\n UserGuide : cube function:returns the cube of any number")
               Cube_Input = int(input("\nEnter the  value:"))
               print("The cube output of Given value :",numbers.cube(Cube_Input))
            elif Number_Input == "11":
               print("\n\n UserGuide : cube root function:returns the cube root of any number")
               Cubert_Input = int(input("\nEnter the value:"))
               print("The cube root output of Given value :",numbers.cube_root(Cubert_Input))
            elif Number_Input == "12":
               print("\n\n UserGuide : prime function:returns the number prime or not")
               prime_Input = int(input("\nEnter the value:"))
               numbers.prime(prime_Input)
            elif Number_Input == "13":
               print("\n\n UserGuide : armstrong function:returns the number armstrong or not")
               armstrong_Input = int(input("\nEnter the value:"))
               numbers.armstrong(armstrong_Input)
            elif Number_Input == "14":
               print("\n\n UserGuide : Fibonacci function:returns the Fibonacci series")
               Fibonacci_Input = int(input("\nEnter the value:"))
               numbers.Fibonacci(Fibonacci_Input)
            elif Number_Input == "15":
               print("\n\n UserGuide : factorial function:returns the factorial number")
               factorial_Input = int(input("\nEnter the value:"))
               print("The factorial of given number :",numbers.factorial(factorial_Input))
            elif Number_Input == "16":
               print("\n\n UserGuide : odd_even function:returns the value is odd or even")
               odd_even_Input = int(input("\nEnter the  value:"))
               numbers.odd_even(odd_even_Input)
            elif Number_Input == "17":
               print("\n\n UserGuide : Postive_Negative function:returns the value is Positive or Negative")
               Postive_Negative_Input = int(input("\nEnter the value:"))
               numbers.Postive_Negative(Postive_Negative_Input)

            else:
                print("Exiting...")
                break

#------------------------------String Function-------------------------------------------------------#

    elif UserChoice == "2":
    
        
        String_dict = {"1": "Length","2":"reverse","3":"Join","4":
                       "split","5":"palindrome","6":"Add Two String",
                       "7":"startswith","8":"endswith","9":"ASCII(Char)",
                       "10":"vowels","11":"replace","12":"Exit"}
        while True:
            print('\n\n "Available Functions in string:"\n\n',String_dict)
    
            import strings
            String_Input = input("\n\nSelect any one number to perform the operation:")
            if String_Input == "1":
                print("\n\n UserGuide : Length function: Used to identify the length")
                Length_Input = input("\nEnter the value:")
                print("The length of given string:\n",strings.length(Length_Input))
            elif String_Input == "2":
                print("\n\n UserGuide : Reverse function: Used to reverse the string")
                reverse_Input = input("\nEnter the value:")
                print("The revesed string :\n",strings.reverse(reverse_Input))
            elif String_Input == "3":
                print("\n\n UserGuide : Join function: Joins the elements of an iterable to the end of the string")
                print("Output :\n",strings.join())
            elif String_Input == "4":
                print("\n\n UserGuide : split function: Splits the string at the specified separator, and returns a list")
                Split_Input = input("\nEnter the value:")
                print("Output :\n",strings.split(Split_Input))
            elif String_Input == "5":
                print("\n\n UserGuide : parlindrome function: Used to identify the string is parlindrome or not")
                palindrome_Input = input("\nEnter the value:")
                strings.palindrome(palindrome_Input)
            elif String_Input == "6":
                print("\n\n UserGuide : Add Two String function: Used to ADD two strings")
                Add_Input = input("\nEnter the first string:")
                Add_Input1 = input("\nEnter the second string:")
                print("Output:\n",strings.Add_Two_Strings(Add_Input,Add_Input1))
            elif String_Input == "7":
                print("\n\n UserGuide : startswith function: Returns true if the string starts with the specified value")
                startswith_Input = input("\nEnter the full string:")
                startswith_Input1 = input("\nEnter the String startswith to check:")
                print("Output :\n",strings.startswith(startswith_Input,startswith_Input1))
            elif String_Input == "8":
                print("\n\n UserGuide : endswith function: Returns true if the string ends with the specified value")
                endswith_Input = input("\nEnter the full string:")
                endswith_Input1 = input("\nEnter the String endswith to check:")
                print("Output :\n",strings.endswith(endswith_Input,endswith_Input1))
            elif String_Input == "9":
                print("\n\n UserGuide : ASCII(Char) function: used to identify the ASCII character Value")
                ASCII_Input = input("\nEnter the character to check:")
                strings.ASCII(ASCII_Input)
            elif String_Input == "10":
                print("\n\n UserGuide : Vowels function: it will count the vowel in the given string")
                Vowel_Input = input("\nEnter the string to check vowel count:")
                strings.vowels(Vowel_Input)
            elif String_Input == "11":
                print("\n\n UserGuide : replacec function: replaces a specified phrase with another specified phrase.")
                strings.replace()
            else:
                print("Exit")
                break

#-------------------------------------------List Function-------------------------------------------------------------#

    elif UserChoice == "3":
               
        List_dict = {"1":"length","2":"min","3":"max","4":"Append",
                     "5":"insert","6":"sort","7":"Remove","8":"pop",
                     "9":"Concordinate","10":"count","11":"reverse",
                     "12":"extend","13":"copy","14":"clear","15":"del",
                     "16":"RemoveDuplicate","17":"EXIT"}
        while True:
            
            print('\n\n Available Functions in List:\n\n',List_dict)
            import List
            UserListCreation = int(input("Enter the Length of List to be create :\n"))
            CustumList = List.Create_list(UserListCreation)
            UserOperation_Input = input("\n\nSelect any one number to perform the operation:")   
            if UserOperation_Input == "1":
                print("\n\n UserGuide : Length function: Used to identify the length")
                print("The length of given List:\n",List.length(CustumList))
            elif UserOperation_Input == "2":
                print("\n\n UserGuide : Min function: it will return the Minimum value in the list")
                print("\n\nThe Minimum Value in the List:\n",List.minimum(CustumList))
            elif UserOperation_Input == "3":
                print("\n\n UserGuide : Max function: it will return the Maximum value in the list")
                print("\n\nThe maximum Value in the List:\n",List.maximum(CustumList))
            elif UserOperation_Input == "4":
                print("\n\n UserGuide : Append function: it will append the value in existing list")
                List.append(CustumList)
            elif UserOperation_Input == "5":
                print("\n\n UserGuide : insert function: Adds an element at the specified position in the List")
                List.insert(CustumList)
            elif UserOperation_Input == "6":
                print("\n\n UserGuide : sort function: Sorts the list\n")
                List.sort(CustumList)
            elif UserOperation_Input == "7":
                print("\n\n UserGuide : Remove function: Removes the first item with the specified value\n")
                List.remove(CustumList)
            elif UserOperation_Input == "8":
                print("\n\n UserGuide : pop function: Removes the element at the specified position\n")
                List.pop(CustumList)
            elif UserOperation_Input == "9":
                print("\n\n UserGuide : Concordinate function: Adds the two List\n")
                CListCreation = int(input("Enter the Length of List to be create :\n"))
                CList = List.Create_list(CListCreation)       
                print("The List After concordinating :",CustumList + CList)
            elif UserOperation_Input == "10":
                print("\n\n UserGuide : count function: Returns the number of elements with the specified value\n")
                List.count(CustumList)
            elif UserOperation_Input == "11":
                print("\n\n UserGuide : Reverse function: Reverses the order of the list\n")
                List.reverse(CustumList)
            elif UserOperation_Input == "12":
                print("\n\n UserGuide : extend function: Add the elements of a list (or any iterable), to the end of the current list\n")
                ExtendListCreation = int(input("Enter the Length of List to be create :\n"))
                ExtendCustomized = List.Create_list(ExtendListCreation)
                CustumList.extend(ExtendCustomized)
                print("The List value after extending :\n",CustumList)
            elif UserOperation_Input == "13":
                print("\n\n UserGuide : copy function: Returns a copy of the list\n")
                List.copy(CustumList)
            elif UserOperation_Input == "14":
                print("\n\n UserGuide : clear function: Removes all the elements from the list\n")
                List.clear(CustumList)
            elif UserOperation_Input == "15":
                print("\n\n UserGuide : delete function: deletes the list \n")
                List.delete(CustumList)
            elif UserOperation_Input == "16":
                print("\n\n UserGuide : duplicates function: Removes the duplicates in list \n")
                DList = set(CustumList)
                DUList = list(DList)
                print("List After duplicate Removal:",DUList)
            else:
                print("Exiting")
                break
    
#-----------------------------------------------------Tuples---------------------------------------------------------------------------------------#


    elif UserChoice == "4":
        
        

        Tuple_dict = { "1":"count","2":"index","3":"length","4":"slicing","5":"Exit"}
        while True:
                        
            print("\n\nAvailable Functions in Tuples:\n\n",Tuple_dict)
        
    
            import tuples
            UserTupleCreation = int(input("Enter the Length of Tuple to be create :\n"))
            CustumTuple = tuples.Create_Tuple(UserTupleCreation)

            UserTupleOperation_Input = input("\n\nSelect any one number to perform the operation:")
    

            if UserTupleOperation_Input == "1":
                print("\n\n UserGuide : count function: Returns the number of times a specified value occurs in a tuple")
                tuples.count(CustumTuple)
            elif UserTupleOperation_Input == "2":
                print("\n\n UserGuide : index function: Searches the tuple for a specified value and returns the position")
                tuples.index(CustumTuple)
            elif UserTupleOperation_Input == "3":
                print("\n\n UserGuide : length function: provides the length of tuple")
                print("The length of Tuple :",tuples.length(CustumTuple))
            elif UserTupleOperation_Input == "4":
                print("\n\n UserGuide : slicing function: used to slice the tuple")
                print("The Slice output of Tuple :",tuples.slicing(CustumTuple))
            else:
                print("Exiting")
                break


#-------------------------------------------------Set--------------------------------------------------------------------------------------------------#

    elif UserChoice == "5":
        
    
        

        Set_dict = {"1":"add","2":"clear","3":"copy","4":"difference","5":"difference_update","6":"discard","7":"intersection","8":"intersection_update","9":"pop","10":"remove","11":"symmetric_difference","12":"symmetric_difference_update","13":"union","14":"update","15":"Exit"}
        while True:
            print("\n\nAvailable Functions in Sets:\n\n",Set_dict)    
            import sets
            UserSetCreation = int(input("Enter the Length of Set to be create :\n"))
            CustumSet = sets.Create_Set(UserSetCreation)

            UserSetOperation_Input = input("\n\nSelect any one number to perform the operation:")
    
            if UserSetOperation_Input == "1":
                print("\n\n UserGuide : add function: Add the elements to the set")
                sets.AddSet(CustumSet)
            elif UserSetOperation_Input == "2":
                print("\n\n UserGuide : clear function: clear the elements in the set")
                sets.clear(CustumSet)
            elif UserSetOperation_Input == "3":
                print("\n\n UserGuide : copy function: Returns a copy of the set")
                sets.copy(CustumSet)
            elif UserSetOperation_Input == "4":
                print("\n\n UserGuide : difference function :Returns a set containing the difference between two or more sets")
                DifferenceSetInput = int(input("Enter the Length of set to be create to check differencce :\n"))
                DifferenceSet = sets.Create_Set(DifferenceSetInput)
                Dset = CustumSet.difference(DifferenceSet)
                print("Set Value differences:",Dset)
            elif UserSetOperation_Input == "5":
                print("\n\n UserGuide : difference_update function :Removes the items in this set that are also included in another, specified set")
                DifferenceUpdateSetInput = int(input("Enter the Length of set to be create to check difference update :\n"))
                DifferenceUpdateSet = sets.Create_Set(DifferenceUpdateSetInput)
                CustumSet.difference_update(DifferenceUpdateSet)
                print("Set Value difference_update:",CustumSet)
            elif UserSetOperation_Input == "6":
                print("\n\n UserGuide : discard function: Remove the specified item")
                DiscardInput = input("enter the value to dicard:")
                CustumSet.discard(DiscardInput)
                print("OutPut:",CustumSet)
            elif UserSetOperation_Input == "7":
                print("\n\n UserGuide : intersection function: Returns a set, that is the intersection of two other set")
                InterSectionInput = int(input("Enter the Length of set to be create to check intersection :\n"))
                IntersectionSet = sets.Create_Set(InterSectionInput)
                Iset = CustumSet.intersection(IntersectionSet)
                print("Set intersection:",Iset)
            elif UserSetOperation_Input == "8":
                print("\n\n UserGuide : intersection_update function: Removes the items in this set that are not present in other, specified set(s)")
                InterSectionUpdateInput = int(input("Enter the Length of set to be create to check intersection :\n"))
                IntersectionUpdateSet = sets.Create_Set(InterSectionUpdateInput)
                CustumSet.intersection_update(IntersectionUpdateSet)
                print("Set intersection_update:",CustumSet)
            elif UserSetOperation_Input == "9":
                print("\n\n UserGuide : pop function:Removes an element from the set")
                sets.pop(CustumSet)
            elif UserSetOperation_Input == "10":
                print("\n\n UserGuide : remove function:Removes the specified element")
                sets.remove(CustumSet)
            elif UserSetOperation_Input == "11":
                print("\n\n UserGuide : symmetric_difference function: Returns a set with the symmetric differences of two sets")
                symmetric_differenceInput = int(input("Enter the Length of set to be create to check symmetric_difference :\n"))
                symmetric_differenceSet = sets.Create_Set(symmetric_differenceInput)
                Sset = CustumSet.symmetric_difference(symmetric_differenceSet)
                print("Set symmetric_difference:",Sset)
            elif UserSetOperation_Input == "12":
                print("\n\n UserGuide : symmetric_difference_update function: inserts the symmetric differences from this set")
                symmetric_difference_updateInput = int(input("Enter the Length of set to be create to check symmetric_difference :\n"))
                symmetric_difference_updateInputSet = sets.Create_Set(symmetric_difference_updateInput)
                CustumSet.symmetric_difference_update(symmetric_difference_updateInputSet)
                print("Set symmetric_difference_update:",CustumSet)
            elif UserSetOperation_Input == "13":
                print("\n\n UserGuide : union function: Return a set containing the union of sets")
                UnionInput = int(input("Enter the Length of set to be created to check union :\n"))
                UnionSet = sets.Create_Set(UnionInput)
                Uset = CustumSet.union(UnionSet)
                print("Set union output:",Uset)
            elif UserSetOperation_Input == "14":
                print("\n\n UserGuide : update function: Update the set with the union of this set and others")
                updateInput = int(input("Enter the Length of set to be update :\n"))
                UpdateInputSet = sets.Create_Set(updateInput)
                CustumSet.update(UpdateInputSet)
                print("Set Update:",CustumSet)
            else:
                print("Exiting")
                break
        
#-------------------------------------------------------------Dictionaries--------------------------------------------------------------------------#
    
    elif UserChoice == "6":
    
        

        Dictionary = {"1":"clear","2":"copy","3":"fromkeys","4":"get","5":"items","6":"keys","7":"pop","8":"popitem","9":"setdefault","10":"update","11":"values","12":"Exit"}

        while True:

            print("\n\nAvailable Functions in Dictionaries:\n\n",Dictionary)
            
            import dictionaries
    
            UserdictionariesCreation = int(input("Enter the Length of dict to be create :\n"))
            Custumdictionary = dictionaries.Create_dict(UserdictionariesCreation)

            UserDictOperation_Input = input("\n\nSelect any one number to perform the operation:")
    
            if UserDictOperation_Input == "1":
                print("\n\n UserGuide : clear function: Removes all the elements from the dictionary")
                dictionaries.clear(Custumdictionary)
            elif UserDictOperation_Input == "2":
                print("\n\n UserGuide : copy function: copies the dictionary")
                dictionaries.copy(Custumdictionary)
            elif UserDictOperation_Input == "3":
                print("\n\n UserGuide : fromkeys function: Returns a dictionary with the specified keys and value")
                print("OutPut:",dictionaries.fromkeys(Custumdictionary))
            elif UserDictOperation_Input == "4":
                print("\n\n UserGuide : get function: Returns the value of the specified key\n")
                GetInput = input("Enter the Key value:")
                GetOutPut = Custumdictionary.get(GetInput)
                print("output:",GetOutPut)
            elif UserDictOperation_Input == "5":
                print("\n\n UserGuide : items function: Returns a list containing a tuple for each key value pair\n")
                dictionaries.items(Custumdictionary)
            elif UserDictOperation_Input == "6":
                print("\n\n UserGuide : keys function: Returns a list containing the dictionary's keys\n")
                dictionaries.keys(Custumdictionary)
            elif UserDictOperation_Input == "7":
                print("\n\n UserGuide : pop function: Removes the element with the specified key\n")
                dictionaries.pop(Custumdictionary)
            elif UserDictOperation_Input == "8":
                print("\n\n UserGuide : popitem function: Removes the last inserted key-value pair\n")
                dictionaries.popitem(Custumdictionary)
            elif UserDictOperation_Input == "9":
                print("\n\n UserGuide : setdefault function: Returns the value of the specified key. If the key does not exist: insert the key, with the specified value\n")
                UserSetKey = input("Enter the Key:")    
                UserValue = input("Enter the Value:")
                Custumdictionary.setdefault(UserSetKey,UserValue)
                print("Output:",Custumdictionary)
            elif UserDictOperation_Input == "10":
                print("\n\n UserGuide : update function: Updates the dictionary with the specified key-value pairs\n")
                UserSetKey = input("Enter the Key:")    
                UserValue = input("Enter the Value:")    
                Custumdictionary.update({UserSetKey:UserValue})
                print("Output:",Custumdictionary)
            elif UserDictOperation_Input == "11":
                print("\n\n UserGuide : values function: Returns a list of all the values in the dictionary\n")
                dictionaries.values(Custumdictionary)
            else:
                print("Exiting")
                break
        
    else:
        print("Exiting from the calculator")
        break
    
    

    
