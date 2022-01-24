def trouver_maximum_2(a, b):
    if a > b: 
        maximum = a
    else:
        maximum = b
    return maximum

def trouver_maximum_3(a, b, c):
    # on veut trouver le maximum M de a et b
    # puis trouver le maximum entre M et c
    maximum_actuel = trouver_maximum_2(a, b)
    maximum = trouver_maximum_2(maximum_actuel, c)
    return maximum