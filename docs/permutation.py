# def permutation(position, A):
#     if position == 0:
#         print(A)
#         return A
#     else:
#         permutation(position - 1, A)
#         for i in range(position - 1):
#             if position % 2 == 0:
#                 A[position-1], A[i] = A[i], A[position-1]
#             else:
#                 A[position-1], A[0] = A[0], A[position-1]
#             permutation(position - 1, A)


# A = ['Mignonne','Allons voir','ce matin']
# permutation(len(A), A)

nx = 256
ny = 256
image = [[(0,0,0) for i in range(nx)] for j in range(ny)]

def invert_pixel(tup_pix):
    return (255-tup_pix[0], 255-tup_pix[1], 255-tup_pix[2])

def invert_col(table):
    for i, tup in enumerate(table):
        table[i] = invert_pixel(tup)
    return table

def invert_table_table(image):
    for i, table in enumerate(image):
        image[i] = invert_col(table)
    return image

