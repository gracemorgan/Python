def isFibonacci(n):
    if n==0:
        return False
    elif n==1:
        return True
    else:
        return isFibonacci(n-1)+isFibonacci(n-2)

def printList(newlst):
    count=0
    for i in newlst:
        if (isFibonacci(i)):
            if count==4:
                count=0
                print(format(i,"2d"))
            else:
                print(i, end=" ")
                count+=1
def main():
    lst=input("Please enter the numbers:")
    nums=[int(j) for j in lst.split()]

    newlst=[]
    for i in nums:
        if (isFibonacci(i)):
            newlst.append(i)
    printList(newlst)

main()
