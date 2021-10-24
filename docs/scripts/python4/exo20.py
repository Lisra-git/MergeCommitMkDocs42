a = 0
b = 0
def sum_adder(c_0):
    return (c_0 + a + b) % 2

a = 0
b = 1
sum = sum_adder(0)
print(sum)