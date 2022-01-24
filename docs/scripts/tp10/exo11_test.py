b1 = ("déterminer_minimum(8, 2) == 2", "déterminer_minimum(1, 8) == 1", "déterminer_minimum(-1, -2) == -2")
b2 = ("distance_hamming(['c', 'h', 'a', 't'], ['c', 'h', 'a', 't']) == 0", \
    "distance_hamming(['c', 'h', 'i', 'e', 'n'], ['c', 'h', 'i', 'o', 't']) == 2", \
    "distance_hamming(['c', 'h', 'a', 't'], ['c', 'h', 'a', 't', 'o', 'n']) == 2",
    "distance_hamming(['v', 'i', 'd', 'e'], []) == 4")

benchmark = [b1, b2 ]