from functools import lru_cache
@lru_cache(None)
def tribonach(x):
   if x==1:
     return 0
   if x==2:
     return 0
   if x==3:
     return 1
   if x>3:
     return tribonach(x-1)+tribonach(x-2)+tribonach(x-3)
a= [73, 10, 4, 15, 20, 7]
mass=[0,0,0,0,0,0]
for i in range(len(a)):
    mass[i]=tribonach(a[i])
print(mass)