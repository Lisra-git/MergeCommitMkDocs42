def translater(vec_x, vec_y, a, b):
    nouveau_vec_x = vec_x + a
    nouveau_vec_y = vec_y + b
    return nouveau_vec_x, nouveau_vec_y

v_x, v_y = 2, 3
t_x, t_y = 1, 0
print(translater(v_x, v_y, t_x, t_y))