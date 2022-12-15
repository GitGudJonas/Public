############ Aestheticc enter #########
import sympy as sp
####use 1/2=sp.Rational(1,2) to have fractions
matrixA = sp.Matrix([[2,0], [0,2]])
matrixB = sp.Matrix([[1,1], [-1,3]])
############################################################
P, C = matrixA.diagonalize()
Q, D = matrixB.diagonalize()
if C==D:
    R=(P*Q**-1).applyfunc(sp.simplify)
    print("R=",R**-1)
    print("Rinv=",R)
    print(R**-1*matrixA*R)
else:
    print("different eigenvalues")
#### show R**-1*matrixA*R = B inline

