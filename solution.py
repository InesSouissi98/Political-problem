import numpy as np
from scipy.optimize import linprog

A= np.array([[2,-8,0,-10],[-5,-2,0,0],[-3,5,10,2]])
b= np.array([-50,-100,-25])
c= np.array([1,1,1,1])

solution= linprog(c=c,A_ub=A,b_ub=b, method= 'simplex',bounds=(0,None))

solution.fun

solution.x
