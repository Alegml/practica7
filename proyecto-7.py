"""import numpy as np

def Richter(A,d):

  if d<=1:
    B=3.5

  elif d>1 and d<=10:
    B=3

  elif d>10:
    B=2

  M=np.log10(A)+B*np.log10(d)
  return M

Amplitud=float(input("Ingrese la amplitud maxima en mm: "))
distancia=float(input("Ingrese la distancia epicentral en km: "))

Magnitud=Richter(Amplitud,distancia)
print(Magnitud)"""

