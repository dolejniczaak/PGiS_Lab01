from math import sqrt
def miejsca_zerowe(a,b,c):
    delta=((b**2)-(4*a*c))
    x1=0
    x2=0
    if delta==0:
        x1=(-b/2*a)
        return x1
    elif delta>0:
        x1=((-b-sqrt(delta))/(2*a))
        x2=((-b+sqrt(delta))/(2*a))
        return x1, x2
    elif delta<0:
        return None 
def kwadratowa(a,b,c,x):
    y=a*x**2+b*x+c
    return y
wynik = miejsca_zerowe(5,15,10)
print wynik
igrek = kwadratowa(5, 15, 10, 2)
print igrek
