a,b,c=map(float,input().split())
def delta(a,b,c):
  d =  (b**2) - (4 * a * c)
  return d
def raizes1(a,b,c):
  d = delta(a,b,c)
  if d < 0  or a  == 0:  
    return "Impossivel calcular"
  x1 = (-b + d**0.5) / (2 * a)
  return x1
def raizes2(a,b,c):
  d = delta(a,b,c)
  if d < 0  or a == 0:  
    return "Impossivel calcular"
  x2 = (-b - d**0.5) / (2 * a)
  return x2
X1 =  raizes1(a,b,c)
X2 =  raizes2 (a,b,c)
if X1 == "Impossivel calcular":
    print(f'Impossivel calcular')
elif X2 == "Impossivel calcular":
    print(f'Impossivel calcular')
else:
    X1 = float(X1)    
    X2 = float(X2)
    print(f'R1 = {X1:.5f}')
    print(f'R2 = {X2:.5f}')
