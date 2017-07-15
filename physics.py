import numpy as np

def distance(p1, p2) :
    dx = p1.x - p2.x
    dy = p1.y - p2.y
    return np.sqrt(dx * dx + dy * dy)
    

