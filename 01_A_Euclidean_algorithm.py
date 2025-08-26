#question 1:    implement the Euclidean algorithm 




def gcd(a,b):
    if(a==0):
        return b
    elif(b==0):
        return a
    else:
        return gcd(b,a%b)
       
a=int(input("enter a number"))
b=int(input("enter a number"))
c=gcd(a,b)
print(c)   

