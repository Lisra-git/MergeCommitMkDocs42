for lettre in "ABCDEFGH":
    for chiffre in range(8):
        case = lettre + str(chiffre + 1)
        print(case, end = ' ')
    print()