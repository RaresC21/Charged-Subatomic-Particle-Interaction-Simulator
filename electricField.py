import physics
from particle import *

class Electric_Field (object) :
    
    def __init__ (self, objs) :
        self.particle = objs
                    
    def force_vec (self, x, y) :
        Ex = 0.0
        Ey = 0.0

        for ob in self.particle :
            test = Particle(x,y, 0)
            d = physics.distance(ob, test)
            if d <= 0.01 : 
                continue
            else :
                (ex, ey) = electricField(ob, test)

                Ex = Ex + ex
                Ey = Ey + ey

        return (Ex, Ey, False)

def electricField(particle, test) :
	r = physics.distance(particle, test)
	magnitude = particle.charge / (r * r)
	
	# split into components
	ex = magnitude * (test.x - particle.x) / r
	ey = magnitude * (test.y - particle.y) / r
		
	return (ex, ey)






