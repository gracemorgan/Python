def ispow2(n):
    n = n/2.0
    if n == 2 or n==1:
        return True
    elif n > 2:
        return ispow2(n)
    else:
        return False


def print5(lst):
    count=0
    for i in lst:
        if (ispow2(i)):
            if count==4:
                count=0
                print (i)
            else:
                print(i,end=' ')
                count+=1
            
def main():
    lst = input("Please enter the list")
    nums = [int(j) for j in lst.split()]

    newlst = []
    for i in nums:
        if (ispow2(i)):
            newlst.append(i)

    print5(newlst)
    
main()
