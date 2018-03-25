import math

L = float(input())  # length can be either integer or float
A = float(input())

for T in range(0, 10):  # loop for the function of X(T) which T equals to the values 0 to 9 
    print(L*math.cos(A*math.cos(T*math.sqrt(9.8/L)))-L*math.cos(A))
