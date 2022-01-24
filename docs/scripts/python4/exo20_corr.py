# a = 0 inutile
# b = 0 inutile

# a et b deviennent des paramètres.
def sum_adder(c_0, a, b):
    return (c_0 + a + b) % 2

# initialisation des variables
bit_a = 0
bit_b = 1
retenue = 0

# appel à la fonction avec 3 paramètres
sum = sum_adder(retenue, bit_a, bit_b)
print(sum)