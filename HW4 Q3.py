password=input("Enter the password:")

def isValid(password):
    num="0123456789"
    num_nums=0
    upperalpha=0
    loweralpha=0
    symbols=0
    for i in password:
        if ord(i)>=ord('A') and ord(i)<=ord('Z'):
            upperalpha+=1
        if i in num:
            num_nums+=1
        if ord(i)>=ord('a') and ord(i)<=ord('z'):
            loweralpha+=1
        if not((ord(i)>=ord('a') and ord(i)<=ord('z')) or(ord(i)>=ord('A') and ord(i)<=ord('Z')) or (i in num)):
            symbols +=1
              
    for i in password:
            if len(password)>=7:
                if num_nums>0:
                    if upperalpha>0:
                        if loweralpha>=0:
                            if symbols==0:
                               return True
    return False


if isValid(password)==True:
    print("The password is valid")
else:
    print("The password is not valid")
   
    
            
 
    
        
        
        
         

