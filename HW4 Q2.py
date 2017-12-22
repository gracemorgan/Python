n=int(input("Enter n:"))

def factor(n):
    i=2
    for i in range (2, n-1):
        if n%i==0:
            return i
    return -1

print("The smallest divisor is:",factor(n))

        
