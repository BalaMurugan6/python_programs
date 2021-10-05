
#to solve quadratic equation
import cmath
a=1
b=5
c=6
x=(b**2)-(4*a*c)
sol1=(-b-cmath.sqrt(x))/(2*a)
sol2=(-b+cmath.sqrt(x))/(2*a)
print("the solutions are {} and{}".format(sol1,sol2) )