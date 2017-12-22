def func1(x):
    if x>1:
        return func2(x-1)
    return 1
def func2(x):
    if x>1:
        return x+1
    return 1
def main():
    print(func1(3))

main()
