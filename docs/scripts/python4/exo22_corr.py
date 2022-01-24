def appartenir_disque(x, y, x_c, y_c, rayon):
    """
    
    """
    if (x - x_c)**2 + (y - y_c)**2 <= rayon**2:
        return True
    else:
        return False