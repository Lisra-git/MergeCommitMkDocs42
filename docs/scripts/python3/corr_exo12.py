u = 15 # initialisation
temps_vol = 0

while u != 1:
   print(u, temps_vol)
   if u % 2 == 0:
      u = u // 2
   else:
      u = 3 * u + 1
   temps_vol += 1

print(u, temps_vol)
