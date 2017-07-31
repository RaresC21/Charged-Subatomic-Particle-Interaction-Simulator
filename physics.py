import numpy as np

def distance(p1, p2) :
    dx = p1.x - p2.x
    dy = p1.y - p2.y
    return np.sqrt(dx * dx + dy * dy)
    

def simulate (particles, ef, lmbda, iterations, step_size) :    

    k = 0
    while (k < iterations) :
    
        for i in range(len(particles)) :

            step(particles[i], lmbda)
            if (k % step_size == 0) :
                particles[i].xs.append(particles[i].x)
                particles[i].ys.append(particles[i].y)           
            
            update(particles[i], ef, lmbda)
        k += 1

def step(particle, lmbda) :
    particle.x += particle.vx * lmbda +  particle.ax * (lmbda ** 2)
    particle.y += particle.vy * lmbda +  particle.ay * (lmbda ** 2)

def update(particle, ef, lmbda):
    Ex, Ey, s = ef.force_vec(particle.x, particle.y) 
    Fx = Ex * particle.charge
    Fy = Ey * particle.charge
            
    particle.vx += particle.ax * lmbda
    particle.vy += particle.ay * lmbda       
            
    particle.ax = Fx / particle.mass
    particle.ay = Fy / particle.mass
    return particle