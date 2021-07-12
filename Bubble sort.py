lst = [6,1,4,2,7,5,3] #the list we want to sort
swapped = True #boolean value, changed when a swap is made
steps = 0       #counts how many steps until list is fully sorted

            
def BubbleSort(lst, swapped, steps):
    while(swapped): #loops whilst swapped is true
        swapped = False #sets swapped to false, unless a swap is made the loop will end after the iteration
        for i in range(len(lst)-1): #loops through the list
            if(lst[i] > lst[i+1]): #if the value at index i is greater than the value one in front of it
                lst[i], lst[i+1] = lst[i+1], lst[i] #we swap the values
                print(lst) #list is printed to show swap
                steps+= 1 #we add one to the number of steps we've done
                swapped = True #we set swapped to true so loop continues after this iteration
    print(lst, "sorted after", steps, "steps") #when the loop ends, sorted list and number of steps to sort are printed
                

        
        
            
BubbleSort(lst, swapped, steps) #calls the function
                    
                    

                

            
                
                
    

