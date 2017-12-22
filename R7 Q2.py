n=int(input("Please enter the size of the list:"))
lst=[]
i=0
for i in range(0,n):
    print("Please enter the elements:",i+1)
    element=int(input())
    lst.append(element)
    i+=1
print("The list you entered is",lst)
counter=lst.count(lst[0])
common=lst[0]
for i in range(n):
    if lst.count(lst[i])>counter:
        common=lst[i]
        counter=lst.count(lst[i])
print("The most common element is",common)       




        
   
    
