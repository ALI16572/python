a = 10
b = 12.5
if type (a) is int:
    print("a is in integer.")
else:
    print("a is not a integer.")

if type (b) is float:
    print("b is a float.")
else:
    print("b is not a float.")    
c = "Hello"   
if type (c) is str:
    print("c is a string.")
else:
    print("c is not a string.")    

x = 3
y = 9

print(x is y)
if x is not y :
    print(" x and y are different")
    