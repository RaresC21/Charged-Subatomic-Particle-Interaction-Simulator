
class Particle (object) :  
    def __init__ (self, x,y, charge) :
        self.x = x
        self.y = y
        self.charge = charge
        
        self.mass = 1      
        
        self.ax = 0     #acceleration
        self.ay = 0
    
        self.vx = 0     #velocity
        self.vy = 0        
        
        # keep list of positions particle is in. 
        self.xs = [x]
        self.ys = [y]
