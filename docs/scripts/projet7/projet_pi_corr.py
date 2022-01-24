from math import sqrt, pi

C1 = 1103
C2 = 26390
C3 = 396

class HPC:

    def __init__(self, n):
        self.n = list(str(n))
    
    def __str__(self):
        print(self.n)
        return str(self.n)

    def __add__(self, HPC):
        c = 0
        

    def __mult__(self, HPC):
        self.n
    

def factorielle(n):
    """ 
    Calcule la factorielle d'un nombre n
    Usage : factorielle(4) renvoie 4*3*2 = 24
    """
    f = 1
    for i in range(n,0,-1):
        f *= i
    return f

i=0
s1 = (2*sqrt(2)/9801 * (factorielle(4*i)*(C1+C2*i))/(factorielle(i)**4*C3**(4*i)))
print(1/s1, s1)
i=1
s2 = (2*sqrt(2)/9801 * (factorielle(4*i)*(C1+C2*i))/(factorielle(i)**4*C3**(4*i)))
print(1/s2, s2)
i=2
s3 = (2*sqrt(2)/9801 * (factorielle(4*i)*(C1+C2*i))/(factorielle(i)**4*C3**(4*i)))
print(1/s3, s3)

print(factorielle(120))
print(HPC(134567898765433456789134567898765433456789134567898765433456789134567898765433456789))