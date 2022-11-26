# This algorithm uses swap method to sort values in a list
# Solution for Task 1 question 3
# Sorts list in ascending order

def sort(ArgumentList): #Define sort() function
    # Initialize ranges
    #We initialize from Zero[0] since python Indexes start from 0 to avoid confusion
    initialization = 0 
    #We use list length as end_range since We're using > or < symbol to compare
    #Hence the extra Index won't be used
    end_range = len(ArgumentList) 
    
    # We use nested for loop to create a loop which sorts the list
    for i in range(initialization,end_range):
        for j in range(initialization,end_range):
            if i<j and ArgumentList[i]>ArgumentList[j]:
                # This statements swaps elements in the list
                ArgumentList[i],ArgumentList[j]=ArgumentList[j],ArgumentList[i]
    print(ArgumentList)
    
        
list1=[1,5,4,64,5,24,48,356,454,652,521,25,41,651,5,264,5,2,4,35,447,626,515,253,412,164,50,20,43,353,440,624,61]
sort(list1)