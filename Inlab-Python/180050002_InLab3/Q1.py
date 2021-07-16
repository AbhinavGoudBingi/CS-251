import math
n = int(input(""))
l = [int(i) for i in input().split()]
def isSquare(n):
    if n<0:
        return False
    else:
        if n==0 or n==1 :
          return True
        else:
          for i in range(int(n/2)+1):
            if (i*i)==n:
                return True
        return False
for i in range(n):
       if(isSquare(l[i])):
          print(l[i],"is a square number")
       else:
          print(l[i],"is not a square number")