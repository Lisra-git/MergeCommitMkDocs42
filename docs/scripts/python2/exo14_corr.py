n = 1492

if n % 400 == 0:
    print(n, " est bissextile.")
elif n % 100 == 0:
    print(n, " n'est pas bissextile.")
elif n % 4 == 0:
    print(n, " est bissextile.")
else:
    print(n, " n'est pas bissextile.")