input1=input("Enter list:")
lst1=[int(i) for i in input1.split()]

input2=input("Enter list 2:")
lst2=[int(j) for j in input2.split()]

def output(lst1,lst2):
    j=0
    i=0
    lst3=[ ]

    while lst1 and lst2 :
        if i<=len(lst1) or j<=len(lst2):
            if i==len(lst1):
               lst3=lst3+(lst2[j:])
            if j==len(lst2):
                lst3=lst3+(lst1[i:])
            if i<=j:
                lst3.append(lst1[i])
            else:
                lst3.append(lst2[j])
                        
       
print(output(lst1,lst2))



